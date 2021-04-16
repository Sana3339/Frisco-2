"""CRUD operations."""

from model import db, Neighborhood, Posting, User, Image_of_Posting, Image_of_Neighborhood, Restaurant, connect_to_db

def create_neighborhood(neighborhood_id, name, latitude, longitude,
                        short_desc, long_desc, median_rent,
                        median_home_price, walk_score, transit_score,images):
    """Create and return a new neighborhood."""

    neighborhood = Neighborhood(neighborhood_id=neighborhood_id,
                                name=name,
                                latitude=latitude,
                                longitude=longitude,
                                short_desc=short_desc,
                                long_desc=long_desc,
                                median_rent=median_rent,
                                median_home_price=median_home_price,
                                walk_score=walk_score,
                                transit_score=transit_score,
                                images=images)

    db.session.add(neighborhood)
    db.session.commit()

def get_neighborhood_by_id(neighborhood_id):
    """Provided a neighborhood_id, return the neighborhood object."""

    neighborhood = Neighborhood.query.get(neighborhood_id)

    return neighborhood

def create_list_of_neighborhood_images(neighborhood_id):

    neighborhood = Neighborhood.query.get(neighborhood_id)
    str_of_images = neighborhood.images
    list_of_images = str_of_images.rsplit(",")

    return list_of_images



def create_user(email, password):
    """Create a new user in the database."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

def create_posting(neighborhood_id, user_email, date, title, desc, contact_info):
    
    posting = Posting(neighborhood_id=neighborhood_id,
                        user_email=user_email,
                        date=date,
                        title=title,
                        desc=desc,
                        contact_info=contact_info,
                        )

    db.session.add(posting)
    db.session.commit()

def get_postings(neighborhood_id):

    postings = Posting.query.filter_by(neighborhood_id=neighborhood_id).all()
    
    return postings


def add_image_to_neighborhood(neighborhood_id, image_of_neighborhood):
    """Provided image details, add to neighborhood images table and link to the correct neighborhood."""

    image_of_neighborhood = Image_of_Neighborhood(neighborhood_id=neighborhood_id,
                                    image_of_neighborhood=image_of_neighborhood)

    db.session.add(image_of_neighborhood)
    db.session.commit()


def get_image_for_neighborhood(neighborhood_id):
    """Provided a neighborhood, return images for that neighborhood."""

    images = Image_of_Neighborhood.query.filter_by(neighborhood_id=neighborhood_id).all()

    return images


# from model import db, User, Movie, Rating, connect_to_db

# def create_user(email, password):
#     """Create and return a new user."""

#     user = User(email=email, password=password)

#     db.session.add(user)
#     db.session.commit()

#     return user


# def get_users():
#     """Return a list of all users."""

#     return User.query.all()  

# def get_user_by_email(email):
#     """Given an email, return a user."""
        
#     return User.query.filter(User.email == email).first()
        

# def create_movie(title, overview, release_date, poster_path):
#     """Create and return a new movie."""

#     movie = Movie(title=title, 
#                   overview=overview, 
#                   release_date=release_date, 
#                   poster_path=poster_path)

#     db.session.add(movie)
#     db.session.commit()

#     return movie

# def get_movies():
#     """Return a list of all movies in the database."""

#     return Movie.query.all()


# def get_movie_by_id(movie_id):
#     """Provided a movie_id, return the movie object."""

#     movie = Movie.query.get(movie_id)

#     return movie


# def create_rating(user, movie, score):
#     """Create a new rating for a movie and return the rating."""

#     rating = Rating(user=user, movie=movie, score=score)

#     db.session.add(rating)
#     db.session.commit()

#   return rating    


if __name__ == '__main__':
    from server import app
    connect_to_db(app)