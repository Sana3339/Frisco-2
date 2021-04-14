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

#hardcoding a neighborhood and place_id for testing purposes
neighborhood = "Marina"
place_id = "ChIJW5ygw9aAhYARSNqml-xlEQ4"

@app.route('/')
def homepage():
    """View homepage"""

    return render_template("homepage.html")

@app.route('/map')
def search_map():
    """Show SF neighborhood map"""

    return render_template("map.html")


@app.route('/api/website.json/<place_id>')
def get_restaurant_website(place_id):
    """Send restaurant id to Google Places Search to get website link."""
    
    payload = {"key": GOOG_API_KEY,
                "place_id": place_id,
                "fields": "website" }

    res = requests.get('https://maps.googleapis.com/maps/api/place/details/json', params=payload)

    converted_res = res.json()
    website = converted_res["result"]["website"]
    
    return website


@app.route('/restaurants/<neighborhood>')
def show_restaurant_details(neighborhood):
    """Show a list of restaurants"""

    payload = {"query": f"restaurants in {neighborhood}",
                "key": GOOG_API_KEY}

    res = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json', params=payload)

    search_results = res.json()
    
    for i in range(5):
        place_id = search_results["results"][i].get("place_id")
        website = get_restaurant_website(place_id)
        data = search_results["results"]
        data[i]["website"] = website

    #return jsonify(data)
    return render_template('restaurant_details.html', data=data)

@app.route('/neighborhood/<neighborhood_id>')
def show_neighborhood(neighborhood_id):
    """Show SF neighborhood details"""

    title = neighborhood_id
    description = "Beautiful neighborhood by the water"
    median_home = "1,000,000"
    median_rental = "$2418"
    walk_score = "98"
    transit_score = "75"
    restaurant_list = get_api_details(neighborhood_id)

    return render_template("neighborhood.html", 
                            name=title,
                            description=description,
                            median_home=median_home,
                            median_rental=median_rental,
                            walk_score=walk_score,
                            transit_score=transit_score,
                            restaurant_list=restaurant_list
                            )






#------------------------------------------#
@app.route('/movies')
def show_movies():
    """List all movies"""

    movies = crud.get_movies()

    return render_template("all_movies.html", movies=movies)


@app.route('/users')
def show_users():
    """List details of all users."""

    users = crud.get_users()

    return render_template("users.html", users=users)


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
        session['current_user'] = user.user_id
        flash(f'Login Success {email}')

        return redirect('/')
            
    else:

        flash('Incorrect try again')
        return redirect('/login')


@app.route('/movies/<movie_id>')
def show_movie_details(movie_id):
    """List details of a particular movie given its movie_id"""

    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie=movie)




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
