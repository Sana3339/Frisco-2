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
    'neighborhood_id': 'bernal',
    'name': 'Bernal Heights',
    'latitude': 37.7389,
    'longitude': -122.4152,
    'short_desc': """<div style='float:right'><img src='/static/img/bernal1.jpeg' width="120" 
                    height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    <b>Bernal Heights</b> is a primarily residential neighborhood with a commercial strip 
                    and a farmer's market every Saturday.
                    <a href="/neighborhood/bernal">Click here to learn more.</a>""",
    'long_desc': """"The neighborhood is primary residential with a commercial strip along
                    Corland Ave featuring restaurants, bars, bakeries, a fish and butchery 
                    shop and more.  It's home to the open-air Alemany Farmers' Market, 
                    one of the oldest extant farmers' markets in the US.  Bernal has not 
                    gentrified to the extent of its neighbor Noe Valley, but gentrification 
                    and property values are increasing as urban professionals replace 
                    working-class home owners and renters""",
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
    'short_desc': """<div style='float:right'><img src='/static/img/castro1.jpeg' width="120" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    The <b>Castro</b> was one of the first gay neighborhoods in the US.
                    It's currently among the most prominent symbols of lesbian, gay,
                    bisexual and transgender (LGBT) activism and events in the world.
                    <a href="/neighborhood/castro">Click here to learn more.</a>""",
    'long_desc': """The Castro was one of the first gay neighborhoods in the US. One of its more
                    notable features is Castro Theatre, a movie palace built in 1922 and one of 
                    San Francisco's premier movie houses. 18th and Castro is a major intersection 
                    where many historic events, marches, and protests have taken and continue to take place.
                    The Castro is a "thriving marketplace for all things gay" meaning everything in the area is 
                    catered to people who identify with LGBT culture and other associated meanings to the word gay.
                    There are cafes, the Castro Theater, and many businesses that cater to or openly welcome LGBT consumers. 
                    These establishments make the Castro an area of high spending and lead to high tourist traffic.""",
    'median_rent': 0,
    'median_home_price': 0,
    'walk_score': 99,
    'transit_score': 95,
    'images': '/static/img/castro1.jpeg'         
    },
    {
    'neighborhood_id': 'haight',
    'name': 'Haight-Ashbury',
    'latitude': 37.7692,
    'longitude': -122.4481,
    'short_desc': """<div style='float:right'><img src='/static/img/haight1.jpeg' width="120" height="120"></div>
                    <div style='float:left; height:130px; width:180px;'><b>Haight-Ashbury</b> 
                    is known as a main center of the 
                    hippie and counterculture of the 1960s. The Summer of Love (1967)
                    has been synonymous with the neighborhood ever since.
                    <a href="/neighborhood/haight">Click here to learn more.</a>""",
    'long_desc': """Haight-Ashbury is known as one of the main centers of the 
                    hippie and counterculture of the 1960s. The mainstream media's 
                    coverage of hippie life in the Haight-Ashbury drew the attention 
                    of youth from all over America. Hunter S. Thompson labeled the 
                    district "Hashbury" in The New York Times Magazine, and the 
                    activities in the area were reported almost daily. The Haight-Ashbury 
                    district was sought out by hippies to constitute a community based 
                    upon counterculture ideals, drugs, and music. This neighborhood 
                    offered a concentrated gathering spot for hippies to create a social 
                    experiment that would soon spread throughout the nation""",
    'median_rent': 3094,
    'median_home_price': 0,
    'walk_score': 97,
    'transit_score': 80,
    'images': '/static/img/haight1.jpeg'   
    },
    {
    'neighborhood_id': 'marina',
    'name': 'Marina',
    'latitude': 37.8037,
    'longitude': -122.4368,
    'short_desc': """<div style='float:right'><img src='/static/img/marina1.jpeg' width="120" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    The <b>Marina</b> has the highest non-Hispanic white resident percentage of any neighborhood in SF. 
                    Chestnut Street is an attraction, lined with stores, restaurants, coffee shops and bars.
                    <a href="/neighborhood/marina">Click here to learn more.</a>""",
    'long_desc': """Gorgeous neighborhood on the marina with beautiful weather.
                    It's most famous for the Palace of Fine Arts.
                    """,
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
    'short_desc': """<div style='float:right'><img src='/static/img/mission1.jpg' width="120" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    The <b>Mission</b> has been the center of the city's Chicano/Mexican-American community
                    and is often warmer and sunnier than other parts of the city.
                    <a href="/neighborhood/mission">Click here to learn more.</a>""",
    'long_desc': """The Mission has historically been the center of the city's Chicano/Mexican-American community
                    and is often warmer and sunnier than other parts of San Francisco.
                    The microclimates of San Francisco create a system by which each neighborhood 
                    can have different weather at any given time, although this phenomenon tends 
                    to be less pronounced during the winter months.
                    The Mission includes four recognized sub-districts. The northeastern 
                    quadrant, adjacent to Potrero Hill is known as a center for high tech startup
                     businesses including some chic bars and restaurants. 
                    The northwest quadrant along Dolores Street is famous for Victorian mansions
                     and the popular Dolores Park 
                    at 18th Street. Two main commercial zones, known as the Valencia corridor 
                    (Valencia St, from about 15th to 22nd) 
                    and the 24th Street corridor known as Calle 24 in the south central part of 
                    the Mission District are both very popular destinations
                     for their restaurants, bars, galleries and street life.
                 """,
    'median_rent': 2911,
    'median_home_price': 0,
    'walk_score': 99,
    'transit_score': 85,
    'images': '/static/img/mission1.jpg, /static/img/mission2.jpeg, /static/img/mission3.jpeg'        
    },
    {
    'neighborhood_id': 'financial',
    'name': 'Financial District',
    'latitude': 37.7946,
    'longitude': -122.3999,
    'short_desc': """<div style='float:right'><img src='/static/img/financial1.jpeg' width="120" height="120"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    The <b>Financial District</b> serves as SF's main business district.
                    It's home to the city's largest concentration of corporate headquarters, law firms,
                    real estate firms and other financial institutions.
                    <a href="/neighborhood/financial">Click here to learn more.</a>""",
    'long_desc': """The Financial District serves as San Francisco's main central business district.
                 All 6 San Francisco Fortune 500 companies are located in the district.  The area is
                marked by a cluster of high-rise towers and several shopping malls including the
                Ferry Building Marketplace where a farmer's market is held every Saturday.
                """,
    'median_rent': 0,
    'median_home_price': 0,
    'walk_score': 99,
    'transit_score': 100,
    'images': '/static/img/financial1.jpeg'     
    },
    {
    'neighborhood_id': 'nob',
    'name': 'Nob Hill',
    'latitude': 37.7930,
    'longitude': -122.4161,
    'short_desc': """<div style='float:right'><img src='/static/img/nob1.jpeg' width="120" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    <b>Nob Hill</b> Nob Hill is known for its numerous luxury hotels and historic mansions.
                    It has historically served as a center of San Francisco's upper class.
                    <a href="/neighborhood/nob">Click here to learn more.</a>""",
    'long_desc': """Nob Hill is known for its numerous luxury hotels and historic mansions.
                    It has historically served as a center of San Francisco's upper class.
                    It's among the highest-income neighborhoods in the US as well as one
                    of the most desirable and expensive real estate markets in the country.

                    Nob Hill is a luxury destination in San Francisco, owing to its numerous
                    Michelin-starred restaurants, boutiques, cultural institutions, art galleries,
                    and historic landmarks.""",
    'median_rent': 2491,
    'median_home_price': 0,
    'walk_score': 99,
    'transit_score': 100,
    'images': '/static/img/nob1.jpeg'    
    },
    {
    'neighborhood_id': 'noe',
    'name': 'Noe Valley',
    'latitude': 37.7502,
    'longitude': -122.4337,
    'short_desc': """<div style='float:right'><img src='/static/img/noe1.jpg' width="120" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    <b>Noe Valley</b> is home to many young professional
                    couples with children and is known as 'Stroller Valley'. Its microclimate is 
                    sunnier and warmer than other neighborhoods. 
                    <a href="/neighborhood/noe">Click here to learn more.</a>""",
    'long_desc': """Noe Valley started out as a working-class neighborhood for employees and 
                    their families in the area's once-thriving blue-collar economy. 
                    Since 1980 it has undergone successive waves 
                    of gentrification and is now considered an upper-middle class/wealthy 
                    neighborhood. It is home to many urban professionals, particularly young 
                    couples with children. It is colloquially known as Stroller Valley, 
                    for the many strollers in the neighborhood. 
                    One of the attractions of Noe Valley is that the adjacent 
                    Twin Peaks partly blocks the coastal fog and cool winds from the 
                    Pacific, making the microclimate usually sunnier and warmer than 
                    surrounding neighborhoods.
                """,
    'median_rent': 2815,
    'median_home_price': 0,
    'walk_score': 92,
    'transit_score': 73,
    'images': '/static/img/noe1.jpg'      
    },
    {
    'neighborhood_id': 'north',
    'name': 'North Beach',
    'latitude': 37.8061,
    'longitude': -122.4103,
    'short_desc': """<div style='float:right'><img src='/static/img/north1.jpeg' width="120" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    <b>North Beach</b> has many Italian restaurants
                    and is one of SF's main nightlife districts as well as a 
                    residential neighborhood populated with young urban professionals, 
                    families, and Chinese immigrants. 
                    <a href="/neighborhood/north">Click here to learn more.</a>""",
    'long_desc': """"
                """,
    'median_rent': 2814,
    'median_home_price': 0,
    'walk_score': 99,
    'transit_score': 95,
    'images': '/static/img/north1.jpeg'    
    },
    {
    'neighborhood_id': 'pac',
    'name': 'Pacific Heights',
    'latitude': 37.7925,
    'longitude': -122.4382,
    'short_desc': """<div style='float:right'><img src='/static/img/pac1.jpg' width="120" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    <b>Pacific Heights</b> has panoramic views of the Golden Gate Bridge, 
                    San Francisco Bay, the Palace of Fine Arts and the Presidio.
                    It is SF's most expensive neighborhood.
                    <a href="/neighborhood/pac">Click here to learn more.</a>""",
    'long_desc': """In 2013, Pacific Heights was named the most expensive neighborhood in the United States. 
                    The article stated that if San Francisco's Pacific Heights had its own zip code, it would be 
                    the most expensive place to live in the United States. 

                    Pacific Heights features two parks, Lafayette and Alta Plaza. Visible to the 
                    north are the Golden Gate Bridge, the Marin Headlands, and Alcatraz Island. 
                    Visible to the south are Twin Peaks and the Sutro Tower.""",
    'median_rent': 2512,
    'median_home_price': 0,
    'walk_score': 96,
    'transit_score': 89,
    'images': '/static/img/pac1.jpg'    
    },
    {
    'neighborhood_id': 'potrero',
    'name': 'Potrero Hill',
    'latitude': 37.7605,
    'longitude': -122.4009,
    'short_desc': """<div style='float:right'><img src='/static/img/potrero1.jpeg' width="120" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    <b>Potrero Hill</b> is known for its views of the San Francisco Bay and city skyline, 
                    its proximity to many destination spots, its sunny weather, and having 
                    two freeways and a Caltrain station. 
                    <a href="/neighborhood/potrero">Click here to learn more.</a>""",
    'long_desc': """Potrero Hill is one of the sunniest neighborhoods in San Francisco.
                    It is a residential neighborhood and not considered a tourist destination. 
                    Although it is not the most walkable neighborhood in San Francisco due to 
                    its hills, it is generally considered a convenient location due to its 
                    proximity to offices, shopping, dining, entertainment, 
                    freeways and a Caltrain station. Despite being surrounded by busy 
                    neighborhoods, Potrero Hill is generally quiet and sleepy.""",
    'median_rent': 2992,
    'median_home_price': 0,
    'walk_score': 89,
    'transit_score': 75,
    'images': '/static/img/potrero1.jpeg'     
    },
    {
    'neighborhood_id': 'presidio',
    'name': 'Presidio',
    'latitude': 37.7989,
    'longitude': -122.4662,
    'short_desc': """<div style='float:right'><img src='/static/img/presidio1.jpeg' width="120" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    The <b>Presidio</b> is a park and former U.S. Army military fort. It's characterized 
                    by wooded areas, hills, and scenic vistas overlooking the Golden Gate Bridge, 
                    San Francisco Bay, and the Pacific Ocean.
                    <a href="/neighborhood/presidio">Click here to learn more.</a>""",
    'long_desc': """The Presidio of San Francisco Francisco is a park and former U.S. Army 
                    military fort and is part of the Golden Gate National Recreation Area.
                    A major planned component of the Presidio's park attractions is the 
                    Tunnel Tops project, which would construct a 14-acre park slated to be open
                    for public use in 2021.  It houses several visitors centers and Crissy Field
                    Center, an urban environmental education center with programs for schools, 
                    public workshops, after-school programs, summer camps, and more.""",
    'median_rent': 4738,
    'median_home_price': 0,
    'walk_score': 41,
    'transit_score': 59,
    'images': '/static/img/presidio1.jpeg'   
    },
    {
    'neighborhood_id': 'richmond',
    'name': 'Inner Richmond',
    'latitude': 37.7781,
    'longitude': -122.4673,
    'short_desc': """<div style='float:right'><img src='/static/img/richmond1.jpg' width="120" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    <b>Inner Richmond</b> is known for its Chinese, 
                    Cambodian, Korean, Burmese, and Russian cuisine. It's a diverse
                    area with sizable Chinese and Russian populations.
                    <a href="/neighborhood/richmond">Click here to learn more.</a>""",
    'long_desc': """The Richmond is in many ways defined by its relation to the parks; 
                    bordered by Golden Gate Park on the south, the Pacific Ocean to the west, 
                    and Lincoln Park, Land's End, Mountain Lake Park and the Presidio of 
                    San Francisco to the north, bisected by the Presidio Greenbelt. 
                    It has many influences from the Chinese-American culture. One of its 
                    three commercial strips, Clement Street, 
                    is sometimes called the second Chinatown due to the high concentration 
                    of Chinese establishments.  The Richmond also has deep Irish and 
                    Russian roots and has many Catholic and Orthodox churches.
                """,
    'median_rent': 3205,
    'median_home_price': 38500000,
    'walk_score': 94,
    'transit_score': 77,
    'images': '/static/img/richmond1.jpg'   
    },
    {
    'neighborhood_id': 'russian',
    'name': 'Russian Hill',
    'latitude': 37.8011,
    'longitude': 122.4194,
    'short_desc': """<div style='float:right'><img src='/static/img/russian1.jpeg' width="120" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    Views from the top of <b>Russian Hill</b> extend in several directions, including the Bay Bridge, 
                    Marin County, the Golden Gate Bridge and Alcatraz. Tourists frequent the cable car 
                    line along Hyde Street, which is lined with restaurants and shops.
                    <a href="/neighborhood/russian">Click here to learn more.</a>""",
    'long_desc': """The neighborhood is most famous for Lombard Street, a one-way street 
                    in which the roadway has eight sharp turns that have earned 
                    the street the distinction of being "the crookedest street in the world". 
                    At the northern foot of the hill is Ghirardelli Square, 
                    which sits on the waterfront of the San Francisco Bay, 
                    Aquatic Park, and Fisherman's Wharf, a popular tourist area.
                    Because of the steepness of the hill, many streets are staircases.""",
    'median_rent': 2489,
    'median_home_price': 0,
    'walk_score': 97,
    'transit_score': 93,
    'images': '/static/img/russian1.jpeg'   
    },
    {
    'neighborhood_id': 'soma',
    'name': 'SoMA',
    'latitude': 37.7785,
    'longitude': -122.4056,
    'short_desc': """<div style='float:right'><img src='/static/img/soma1.jpeg' width="120" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    <b>SoMa</b> houses museums, technology companies, warehouses, 
                    auto repair shops, nightclubs, residential hotels, art spaces, 
                    loft apartments, furniture showrooms and condominiums.
                    <a href="/neighborhood/soma">Click here to learn more.</a>""",
    'long_desc': """Many major software and technology companies have headquarters and offices 
                    here and the area is home to The area is also home to the few Big-box 
                    stores in San Francisco such as Costco, REI, Nordstrom Rack, and Best Buy.
                    SOMA is home to many of San Francisco's museums, including SFMOMA, the Yerba 
                    Buena Center for the Arts and more.""",
    'median_rent': 2992,
    'median_home_price': 0,
    'walk_score': 97,
    'transit_score': 100,
    'images': '/static/img/soma1.jpeg'   
    }, 
    {
    'neighborhood_id': 'sunset',
    'name': 'Inner Sunset',
    'latitude': 37.7602,
    'longitude': -122.4703,
    'short_desc': """<div style='float:right'><img src='/static/img/sunset1.jpeg' width="120" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    The <b>Inner Sunset</b> has a variety of local businesses including restaurants, 
                    bars, breweries, book stores, bakeries, ice cream parlors, 
                    clothing stores, a tattoo parlor, a wine bar and more.
                    <a href="/neighborhood/sunset">Click here to learn more.</a>""",
    'long_desc': """The Sunset district has a cool summer mediterranean 
                    climate, albeit with an unusual annual temperature distribution. 
                    The warmest days of the year occur in October and then the coldest 
                    nights of the year occur just two months later in December.

                    There is a year-round, Sunday morning farmers' market offering 
                    California-grown produce, fish, eggs, and meat, as well as local food 
                    vendors and artisans.  

                    Stern Grove, a heavily wooded park and amphitheater, is known 
                    for its annual summer festival.""",
    'median_rent': 2813,
    'median_home_price': 0,
    'walk_score': 95,
    'transit_score': 72,
    'images': '/static/img/sunset1.jpeg'  
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


