"""Models for Frisco app."""

from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime

db = SQLAlchemy()

class Neighborhood(db.Model):
    """A neighborhood."""

    __tablename__='neighborhoods'

    neighborhood_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    latitude = db.Column(db.String, nullable=False, unique=True)
    longitude = db.Column(db.String, nullable=False, unique=True)
    short_desc = db.Column(db.Text, nullable=False)
    long_desc = db.Column(db.Text, nullable=False)
    median_rent = db.Column(db.String, nullable=False)
    median_home_price = db.Column(db.String, nullable=False)
    walk_score = db.Column(db.Integer, nullable=True)
    transit_score = db.Column(db.Integer, nullable=True)
    images = db.Column(db.Text, nullable=True)

    def __repr__(self):

        return f'<id={self.neighborhood_id} name={self.name}>'

class Posting(db.Model):
    """A posting for housing available in a neighborhood."""

    __tablename__ = 'postings'

    posting_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    neighborhood_id = db.Column(db.String, db.ForeignKey('neighborhoods.neighborhood_id'))
    title = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    contact_info = db.Column(db.Text, nullable=False)

    neighborhood = db.relationship( 'Neighborhood', backref='postings')

    def __repr__(self):

        return f'<id={self.posting_id} title={self.title} user={self.user_id} neighborhood={neighborhood_id}>'

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    email = db.Column(db.String, primary_key=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):

        return f'<email={self.email} password={self.password}>'
    

class Image_of_Posting(db.Model):
    """An image belonging to a posting."""

    tablename = 'images_of_postings'

    image_of_posting_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    posting_id = db.Column(db.Integer, db.ForeignKey('postings.posting_id'))
    image = db.Column(db.Text, nullable=False)

    posting = db.relationship('Posting', backref='images_of_postings')

    def __repr__(self):

        return f'<id={self.image_of_posting_id} posting_id={self.posting_id} image={self.image}>'


class Image_of_Neighborhood(db.Model):
    """Image of a neighborhood."""

    __tablename__ = 'images_of_neighborhoods'

    image_of_neighborhood_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    neighborhood_id = db.Column(db.String, db.ForeignKey('neighborhoods.neighborhood_id'))
    image_of_neighborhood = db.Column(db.Text, nullable=False)

    neighborhood = db.relationship('Neighborhood', backref='images_of_neighborhoods')

    def __repr__(self):

        return f'<id={self.image_of_neighborhood_id} neighborhood={self.neighborhood_id} image_link={self.image_of_neighborhood}>'


class Restaurant(db.Model):
    """A restaurant in a neighborhood."""

    __tablename__ = 'restaurants'

    restaurant_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    neighborhood_id = db.Column(db.String, db.ForeignKey('neighborhoods.neighborhood_id'))
    address = db.Column(db.String, nullable = True)
    rating = db.Column(db.String, nullable = True)
    website = db.Column(db.String, nullable = True)
    image = db.Column(db.Text, nullable = True)
    
    neighborhood = db.relationship('Neighborhood', backref='restaurants')

    def __repr__(self):

        return f'<id={self.restaurant_id} name={self.name}> neighborhood={self.neighborhood_id}'

# class User(db.Model):
#     """A user."""

#     __tablename__ = 'users'

#     user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     email = db.Column(db.String, unique=True)
#     password = db.Column(db.String)

#     # ratings = a list of Rating objects

#     def __repr__(self):

#         return f'<User user_id={self.user_id} email={self.email} password={self.password}>'


# class Movie(db.Model):
#     """A movie."""

#     __tablename__ = 'movies'

#     movie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String)
#     overview = db.Column(db.Text)
#     release_date = db.Column(db.DateTime)
#     poster_path = db.Column(db.String)

#     # ratings = a list of Rating objects

#     def __repr__(self):

#         return f'<Movie movie_id={self.movie_id} title={self.title}'

# class Rating(db.Model):
#     """A movie rating."""

#     __tablename__ = 'ratings'

#     rating_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     score = db.Column(db.Integer)
#     movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

#     movie = db.relationship('Movie', backref='ratings')
#     user = db.relationship('User', backref='ratings')

#     def __repr__(self):

#         return f'<Rating rating_id={self.rating_id} score={self.score} movie_id={self.movie_id} user_id={self.user_id}>'



def connect_to_db(flask_app, db_uri='postgresql:///neighborhoods', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)

