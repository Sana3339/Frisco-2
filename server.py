"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db
from jinja2 import StrictUndefined
from datetime import datetime
import requests
import os
import crud
import json



app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

GOOG_API_KEY = os.environ['GOOGLE_API_KEY']

# This is the first page the user sees when coming to the site
@app.route('/')
def homepage():
    """View homepage"""

    return render_template("homepage.html")

#This is the second page the user sees upon entering the site. 
# User can explore neighborhoods or click link to post housing
@app.route('/search_map')
def search_map():
    """Show SF neighborhood map"""

    return render_template("search_map.html")

#After logging in, users can select which neighborhood to post housing in.
@app.route('/postings_map')
def show_postings_map():
    """Show SF neighborhood map for users to select which neighborhood to post housing in."""

    return render_template("postings_map.html")

#This route calls the Google Places Details API providing a restaurant's 'place_id' and returning the
#restaurant's website. This website is appended to the restaurant details in the neighborhood pages
@app.route('/api/website.json/<place_id>')
def get_restaurant_website(place_id):
    """Send restaurant id to Google Places Search API to get restaurant website link."""
    
    payload = {"key": GOOG_API_KEY,
                "place_id": place_id,
                "fields": "website" }

    res = requests.get('https://maps.googleapis.com/maps/api/place/details/json', params=payload)

    converted_res = res.json()
    result = converted_res["result"]
    if result.get('website')!=None:
        website = converted_res["result"]["website"]
    else:
        website = ""
    
    return website

#This route is used for testing purposes to ensure that restaurants for a particular
#neighborhood are returning properly.
@app.route('/restaurants/<neighborhood_id>')
def show_restaurant_details(neighborhood_id):
    """Show a list of restaurants in a specific neighborhood"""

    neighborhood = crud.get_neighborhood_by_id(neighborhood_id)
    neighborhood_name = neighborhood.name

    payload = {"query": f"restaurants in {neighborhood_name} in San Francisco",
                "key": GOOG_API_KEY}

    res = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json', params=payload)

    search_results = res.json()
    data = search_results["results"]

    #I'm creating an empty list to limit the API search results to 5. 
    #This limitation allows us to do a separate API call and add the website to our search results
    #If you don't limit it, you will get a 'key error' for the 'website' field and the page won't load
    limited_data = []

    for i in range(5):
        limited_data.append(data[i])    
    
    for i in range(5):
        place_id = search_results["results"][i].get("place_id")
        website = get_restaurant_website(place_id)
        limited_data[i]["website"] = website

    return limited_data


#This route queries the database for neighborhood-related data and
#gets restaurant data from the show_restaurant_details() function to 
#display to the user
@app.route('/neighborhood/<neighborhood_id>')
def show_neighborhood(neighborhood_id):
    """Show SF neighborhood details"""

    neighborhood = crud.get_neighborhood_by_id(neighborhood_id)
    images = crud.get_image_for_neighborhood(neighborhood_id)

    name = neighborhood.name
    long_desc = neighborhood.long_desc
    median_home_price = neighborhood.median_home_price
    sq_ft_price = neighborhood.sq_ft_price
    median_rental = neighborhood.median_rent
    walk_score = neighborhood.walk_score
    transit_score = neighborhood.transit_score
    neighborhood_images = crud.create_list_of_neighborhood_images(neighborhood_id)
    
    restaurant_data = show_restaurant_details(neighborhood_id)

    return render_template("neighborhood.html", 
                            name=name,
                            description=long_desc,
                            median_home=median_home_price,
                            sq_ft_price=sq_ft_price,
                            median_rental=median_rental,
                            walk_score=walk_score,
                            transit_score=transit_score,
                            restaurant_data=restaurant_data,
                            images=neighborhood_images,
                            neighborhood_id=neighborhood_id
                            )

#This route queries the database to show the user the posted housing
#for a particular neighborhood
@app.route('/housing/<neighborhood_id>')
def show_housing(neighborhood_id):
    """Show housing posted for a neighborhood."""

    postings = crud.get_postings(neighborhood_id)
    neighborhood = crud.get_neighborhood_by_id(neighborhood_id)

    name = neighborhood.name

    return render_template('housing.html', postings=postings,
                                            name=name,
                                            neighborhood_id=neighborhood_id)

#This route is used to get neighborhood details from DB to the front end
#via AJAX requests in the maps JS files. The data is used to populate
#the map markers, info windows and text on the page
@app.route('/neighborhood-details.json')
def get_neighborhood_details():
    """Return specific neighborhood details to populate Google map."""

    neighborhoods_obj = crud.get_all_neighborhoods()

    all_neighborhood_details = []

    for neighborhood in neighborhoods_obj:
        neighborhood_id = neighborhood.neighborhood_id
        name = neighborhood.name
        short_desc = neighborhood.short_desc
        latitude = neighborhood.latitude
        longitude = neighborhood.longitude

        neighborhood_dict = {
            'neighborhood_id': neighborhood_id,
            'name': name, 
            'short_desc': short_desc,
            'latitude': latitude,
            'longitude': longitude,
            }

        all_neighborhood_details.append(neighborhood_dict)
    
    return jsonify(all_neighborhood_details)

#This route shows the user what housing they have posted (if any)
@app.route('/profile/<email>')
def show_user_profile(email):
    """Show user's profile page including their listed housing."""

    name = email.rsplit("@")[0]
    postings = crud.get_user_postings(email)

    return render_template('user_profile.html', name=name,
                                                postings=postings)

#This route shows the account creation and login page
@app.route('/login')
def show_login():
    """Displays the account creation and log in page"""

    return render_template("login.html")



#This route creates a new user via the account creation form
@app.route('/users', methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email) 
    
    if user:
        flash('Email is already registered. Log in if you already have an account.')

    else:
        crud.create_user(email, password)
        flash('Account created successfully')
        session['current_user'] = email

    return redirect('/success_login')

#This route checks if a user is in the database and logs them in if so.
@app.route('/handle-login', methods=['POST'])
def handle_login():
    """Logs in an existing user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user and user.password == password:
        session['current_user'] = email

        return redirect('/success_login')
            
    else:

        flash('Incorrect try again')
        return redirect('/login')

#This route is used in 'search_map' page dispalying which neighborhoods
#users can learn about.  If users click on the 'post housing' link, this 
#route checks if they are logged in before allowing them to post housing.
@app.route('/check_login')
def check_login_at_intro():
    """Check if the user is logged in. If so, redirect to neighborhood selection map page. 
        If not, redirect to login page."""

    if session.get('current_user') is None:
        return redirect('/login')
    
    else:
        return redirect(f'/postings_map')

#If a user clicks on the 'post housing' link from a neighborhood details page,
#this route checks if the user is logged in, and if so, redirects them to the
#specific neighborhood posting page.  If the user isn't logged in, they are 
#redirected to the login page with the neighborhood_id being added to the session.
#This allows the user to be redireced to the neighborhood page immediately after
#login (bypassing the neighborhood selection page)
@app.route('/check_login/<neighborhood_id>')
def check_login_with_neighborhood(neighborhood_id):
    """Check if a user is logged in and add their neighborhood_id to the session."""

    if session.get('current_user') is None:
        session['neighborhood_id'] = neighborhood_id
        return redirect('/login')
    
    else:
        return redirect(f'/post_housing/{neighborhood_id}')


#Depending on if a user came from the home page or from a specific neighborhood's
#housing page, upon successful login, they are redirected to the map page to 
#select a neighborhood to post in or to the specific neighborhood's posting
#page that they were previously visiting.
@app.route('/success_login')
def show_after_login():
    """Upon login, users can post housing or visit their profile page."""

    if session.get('neighborhood_id') is not None:
        neighborhood_id = session['neighborhood_id']
        return redirect(f'/post_housing/{neighborhood_id}')

    else:
        email = session['current_user']
        return redirect(f'/profile/{email}')

#If a user is logged in, they get logged out. If they aren't logged in,
#an error message is displayed
@app.route('/log_out')
def log_out_user():
    
    if session.get('current_user') is None:
        flash('You are not currently logged in.')
        return redirect('/login')

    else:
        session.pop('current_user')
        flash('You have been logged out.')
        if session.get('neighborhood_id') is not None:
            session.pop('neighborhood_id')
        return redirect('/login')
    
#This route displas a from to users wanting to post housing in a particular
#neighborhood.
@app.route('/post_housing/<neighborhood_id>')
def post_housing(neighborhood_id):
    "Display form for logged in user to post available housing."

    neighborhood = crud.get_neighborhood_by_id(neighborhood_id)
    name = neighborhood.name
    session['neighborhood_id'] = neighborhood.neighborhood_id

    return render_template('post_housing.html', name=name)

#This route reads information from the posting form and saves in the database.
@app.route('/handle_posting', methods=['POST'])
def handle_posting():
    """Collects data from post housing form and posts to the database."""
    
    neighborhood_id = session['neighborhood_id']
    email = session['current_user']
    date = datetime.now()
    title = request.form.get("title")
    desc = request.form.get("desc")
    contact_info = request.form.get("contact_info")

    crud.create_posting(neighborhood_id, email, date, title, desc, contact_info)
    
    return redirect(f'housing/{neighborhood_id}')

@app.route('/delete_posting/<posting_id>', methods=['POST'])
def delete_posting(posting_id):
    """Deletes the posting that it's attached to when fired."""

    crud.delete_posting(posting_id)
    email = session['current_user']

    return redirect(f'/profile/{email}')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
