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
    'latitude': '36.6844',
    'longitude': '-121.8022',
    'short_desc': 'By the water',
    'long_desc': 'Gorgeous neighborhood on the marina with beautiful weather',
    'median_rent': '$3,100',
    'median_home_price': '1,200,000',
    'walk_score': '98',
    'transit_score': '75',
    'images': '/static/img/marina1.jpeg'
    },
    {
    'neighborhood_id': 'mission',
    'name': 'Mission',
    'latitude': '37.7599',
    'longitude': '-122.4148',
    'short_desc': 'Great mexican food',
    'long_desc': 'Artistic neighborhood with excellent food and live music',
    'median_rent': '$2,600',
    'median_home_price': '1,000,000',
    'walk_score': '99',
    'transit_score': '85',
    'images': '/static/img/mission1.jpg'        
    },
    {
    'neighborhood_id': 'japantown',
    'name': 'Japantown',
    'latitude': '37.7854',
    'longitude': '-122.4294',
    'short_desc': 'ramen',
    'long_desc': 'cherry blossom festival',
    'median_rent': '$2,600',
    'median_home_price': '1,000,000',
    'walk_score': '99',
    'transit_score': '85',
    'images': '/static/img/japantown1.jpeg'        
    }        
]

neighborhood_id = ""
name = ""
latitude = ""
longitude = ""
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


Create a list of images with which to seed the database

images_of_neighborhoods = [
    {
    'neighborhood_id': 'marina',
    'image_of_neighborhood': '/static/img/marina1.jpeg'
    },
    {
    'neighborhood_id': 'mission',
    'image_of_neighborhood': 'placeholder'        
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


