"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db
import requests
import os
import crud
import json

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

GOOG_API_KEY = os.environ['GOOGLE_API_KEY']


@app.route('/')
def homepage():
    """View homepage"""

    return render_template("homepage.html")

@app.route('/search_map')
def search_map():
    """Show SF neighborhood map"""

    return render_template("search_map.html")

@app.route('/postings_map')
def show_postings_map():
    """Show SF neighborhood map for users to select which neighborhood to post housing in."""

    return render_template("postings_map.html")


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


@app.route('/restaurants/<neighborhood_id>')
def show_restaurant_details(neighborhood_id):
    """Show a list of restaurants in a specific neighborhood"""

    payload = {"query": f"restaurants in {neighborhood_id}",
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

@app.route('/neighborhood/<neighborhood_id>')
def show_neighborhood(neighborhood_id):
    """Show SF neighborhood details"""

    neighborhood = crud.get_neighborhood_by_id(neighborhood_id)
    images = crud.get_image_for_neighborhood(neighborhood_id)

    name = neighborhood.name
    long_desc = neighborhood.long_desc
    median_home_price = neighborhood.median_home_price
    median_rental = neighborhood.median_rent
    walk_score = neighborhood.walk_score
    transit_score = neighborhood.transit_score
    neighborhood_images = crud.create_list_of_neighborhood_images(neighborhood_id)
    
    restaurant_data = show_restaurant_details(neighborhood_id)

    return render_template("neighborhood.html", 
                            name=name,
                            description=long_desc,
                            median_home=median_home_price,
                            median_rental=median_rental,
                            walk_score=walk_score,
                            transit_score=transit_score,
                            restaurant_data=restaurant_data,
                            images=neighborhood_images,
                            neighborhood_id=neighborhood_id
                            )

@app.route('/housing/<neighborhood_id>')
def show_housing(neighborhood_id):
    """Show housing posted for a neighborhood."""

    postings = crud.get_postings(neighborhood_id)
    neighborhood = crud.get_neighborhood_by_id(neighborhood_id)

    name = neighborhood.name

    return render_template('housing.html', postings=postings,
                                            name=name)


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

@app.route('/profile/<user_email>')
def show_user_profile(user_email):
    """Show user's profile page including their listed housing."""

    name = user_email.rsplit("@")[0].title()

    return render_template('user_profile.html', name=name)


@app.route('/login')
def show_login():
    """Displays the account creation and log in page"""

    return render_template("login.html")


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
        flash('Account created successfully.  Please log in.')

    return redirect('/login')

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


@app.route('/success_login')
def show_after_login():
    """Upon login, users can post housing or visit their profile page."""

    return render_template('success_login.html')


@app.route('/post_housing/<neighborhood_id>')
def post_housing(neighborhood_id):
    "Display form for logged in user to post available housing."

    neighborhood = crud.get_neighborhood_by_id(neighborhood_id)
    name = neighborhood.name

    return render_template('post_housing.html', name=name)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
