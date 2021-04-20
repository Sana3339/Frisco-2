"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb neighborhoods')
os.system('createdb neighborhoods')

model.connect_to_db(server.app)
model.db.create_all()

#Create a list of neighborhoods with which to seed the db

neighborhoods = [
    {
    'neighborhood_id': 'marina',
    'name': 'Marina',
    'latitude': 37.8037,
    'longitude': -122.4368,
    'short_desc': '<h3>Beautiful neighborhood by the water. <a href="/neighborhood/marina">Click to learn more</a></h3>',
    'long_desc': 'Gorgeous neighborhood on the marina with beautiful weather',
    'median_rent': 2460,
    'median_home_price': 0,
    'walk_score': 98,
    'transit_score': 75,
    'images': '/static/img/marina1.jpeg, /static/img/marina2.jpeg, /static/img/marina3.jpeg'
    },
    {
    'neighborhood_id': 'mission',
    'name': 'Mission',
    'latitude': 37.7599,
    'longitude': -122.4148,
    'short_desc': 'Artistic neighborhood with excellent food. <a href="/neighborhood/mission">Click to learn more</a>',
    'long_desc': 'Artistic neighborhood with excellent food and live music',
    'median_rent': 2911,
    'median_home_price': 0,
    'walk_score': 99,
    'transit_score': 85,
    'images': '/static/img/mission1.jpg, /static/img/mission2.jpeg, /static/img/mission3.jpeg'        
    },
    {
    'neighborhood_id': 'japantown',
    'name': 'Japantown',
    'latitude': 37.7854,
    'longitude': -122.4294,
    'short_desc': 'Great sushi and ramen. Cherry blossom festival. <a href="/neighborhood/japantown">Click to learn more</a>',
    'long_desc': 'cherry blossom festival',
    'median_rent': 0,
    'median_home_price': 0,
    'walk_score': 99,
    'transit_score': 85,
    'images': '/static/img/japantown1.jpeg, /static/img/japantown2.jpeg, /static/img/japantown3.jpeg'        
    },
    {
    'neighborhood_id': 'bernal',
    'name': 'Bernal Heights',
    'latitude': 37.7389,
    'longitude': -122.4152,
    'short_desc': 'Will fill in later. <a href="/neighborhood/bernal">Click to learn more</a>',
    'long_desc': 'Will fill in later',
    'median_rent': 2704,
    'median_home_price': 0,
    'walk_score': 89,
    'transit_score': 77,
    'images': ''        
    },
    {
    'neighborhood_id': 'castro',
    'name': 'Castro',
    'latitude': 37.7609,
    'longitude': -122.435,
    'short_desc': 'Will fill in later. <a href="/neighborhood/castro">Click to learn more</a>',
    'long_desc': 'Will fill in later',
    'median_rent': 0,
    'median_home_price': 0,
    'walk_score': 99,
    'transit_score': 95,
    'images': ''        
    },
    {
    'neighborhood_id': 'chinatown',
    'name': 'Chinatown',
    'latitude': 37.7941,
    'longitude': -122.4078,
    'short_desc': 'Will fill in later. <a href="/neighborhood/chinatown">Click to learn more</a>',
    'long_desc': 'Will fill in later',
    'median_rent': 0,
    'median_home_price': 0,
    'walk_score': 99,
    'transit_score': 95,
    'images': ''        
    },
    {
    'neighborhood_id': 'diamond',
    'name': 'Diamond Heights',
    'latitude': 37.7424,
    'longitude': -122.4425,
    'short_desc': 'Will fill in later. <a href="/neighborhood/diamond">Click to learn more</a>',
    'long_desc': 'Will fill in later',
    'median_rent': 2999,
    'median_home_price': 0,
    'walk_score': 74,
    'transit_score': 67,
    'images': ''        
    },
    {
    'neighborhood_id': 'civic',
    'name': 'Civic Center',
    'latitude': 37.7941,
    'longitude': -122.4078,
    'short_desc': 'Will fill in later. <a href="/neighborhood/chinatown">Click to learn more</a>',
    'long_desc': 'Will fill in later',
    'median_rent': 2388,
    'median_home_price': 0,
    'walk_score': 0,
    'transit_score': 0,
    'images': ''        
    }
]

neighborhood_id = ""
name = ""
latitude = 0
longitude = 0
short_desc = ""
long_desc = ""
median_rent = ""
median_home_price = ""
walk_score = ""
transit_score = ""
images = ""

for neighborhood in neighborhoods: 
    neighborhood_id = neighborhood['neighborhood_id']
    name = neighborhood['name']
    latitude = neighborhood['latitude']
    longitude = neighborhood['longitude']
    short_desc = neighborhood['short_desc']
    long_desc = neighborhood['long_desc']
    median_rent = neighborhood['median_rent']
    median_home_price = neighborhood['median_home_price']
    walk_score = neighborhood['walk_score']
    transit_score = neighborhood['transit_score']
    images = neighborhood['images']

    crud.create_neighborhood(neighborhood_id, name, latitude, longitude, 
        short_desc, long_desc, median_rent, median_home_price, walk_score, transit_score, images)
                                                     

#Create fake users with which to seed the db

for n in range(10):
    email = f'user{n}@test.com' 
    password = 'test'

    crud.create_user(email, password)

#Create fake postings with which to seed the db

postings = [
    {
    'neighborhood_id': 'marina',
    'user_email': 'user1@test.com',
    'date': datetime.now(),
    'title': 'Beautiful room by the Palace of Fine Arts',
    'desc': 'Gorgeous panoramic views.  Youll be living in a house with 2 other girls.',
    'contact_info': 'Call 415-222-3333'
    },
    {
    'neighborhood_id': 'mission',
    'user_email': 'user2@test.com',
    'date': datetime.now(),
    'title': 'Room available immediately in 2b/2b',
    'desc': 'Great location right by Valencia street with lots of restaurants',
    'contact_info': 'Email user2@test.com',
    }
]

neighborhood_id = ""
user_email = ""
date = ""
title = ""
desc = ""
contact_info = ""

for posting in postings:

    neighborhood_id = posting['neighborhood_id']
    user_email = posting['user_email']
    date = posting['date']
    title = posting['title']
    desc = posting['desc']
    contact_info = posting['contact_info']

    crud.create_posting(neighborhood_id, user_email, date, title, desc, contact_info)


#Will likely delete functions below this line ------------------   

#Create a list of images with which to seed the database

images_of_neighborhoods = [
    {
    'neighborhood_id': 'marina',
    'image_of_neighborhood': '/static/img/marina1.jpeg'
    },
    {
    'neighborhood_id': 'mission',
    'image_of_neighborhood': '/static/img/mission1.jpg'        
    },
    {
    'neighborhood_id': 'japantown',
    'image_of_neighborhood': '/static/img/japantown1.jpeg'        
    }
]

neighborhood_id = ""
image_of_neighborhood = ""

for image in images_of_neighborhoods:
    neighborhood_id = image['neighborhood_id']
    image_of_neighborhood = image['image_of_neighborhood']

    crud.add_image_to_neighborhood(neighborhood_id, image_of_neighborhood)

# #Load movie data from JSON file
# with open('data/movies.json') as f:
#     movie_data = json.loads(f.read())

# # Create fake movies, store them in a list so we can use them 
# # to later create fake ratings
# movies_in_db = []
# for movie in movie_data:

#     title, overview, poster_path = (movie['title'],
#                                    movie['overview'],
#                                    movie['poster_path'])
    
#     release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

#     db_movie = crud.create_movie(title, 
#                                 overview, 
#                                 release_date, 
#                                 poster_path)

#     movies_in_db.append(db_movie)


# for n in range(10):
#     email = f'user{n}@test.com' 
#     password = 'test'

#     user = crud.create_user(email, password)

#     for n in range(10):

#         random_movie = choice(movies_in_db)
#         score = randint(1,5)
        
#         crud.create_rating(user, random_movie, score)


