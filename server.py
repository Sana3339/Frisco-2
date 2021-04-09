"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage"""

    return render_template("homepage.html")

@app.route('/map')
def search_map():
    """Show SF neighborhood map"""

    return render_template("map.html")

@app.route('/neighborhood')
def show_neighborhood():
    """Show SF neighborhood details"""

    return render_template("neighborhood.html")


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

    return redirect('/')


@app.route('/login')
def login_user():
    """Logs in an existing user."""

    email = request.form.get("login_email")
    password = request.form.get("login_password")

    user = crud.get_user_by_email(email)

    if user != None:
        if user.password == password:
            flash('You have successfully logged in!')
            session['user'] = user
        else:
            flash('Incorrect password.  Try again')

    else:
        flash('Email is not registered. Please create an account')

    return render_template("login.html")


@app.route('/movies/<movie_id>')
def show_movie_details(movie_id):
    """List details of a particular movie given its movie_id"""

    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie=movie)




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
