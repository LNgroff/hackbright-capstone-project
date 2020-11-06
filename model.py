"""Models for park finder app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

### See to do list at end of file.

#  TODO: change the "ratings" in the postgresql
def connect_to_db(flask_app, db_uri='postgresql:///parks', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


class User(db.Model):
    """A user"""

    __tablename__ = "users"


    user_id = db.Column(db.Integer,
                primary_key = True,
                autoincrement = True,
                nullable = False)
    username = db.Column(db.String,
                unique = True,
                nullable = False)
    email = db.Column(db.String,
                unique = True,
                nullable = False)
    password = db.Column(db.String,
                nullable = False)

    def __repr__(self):
        return f"""User user_id: {self.user_id}
                        username: {self.username}
                        email: {self.email}"""



class Park(db.Model):
    """A park"""

    __tablename__ = "parks"

    fullname = db.Column(db.Integer,
                primary_key = True,
                autoincrement = True,
                nullable = False)
    park_name = db.Column(db.String,
                unique = True,
                nullable = False)
    state = db.Column(db.String,
                unique = True)
    coordinates = db.Column(db.Integer,
                nullable = False)
    url = db.Column(db.String,
                unique = True,
                nullable = False)
    description = db.Column(db.String)


    def __repr__(self):
        return f"""Park fullname: {self.fullname} 
                name: {self.name}
                state: {self.state}
                coordinates: {self.coordinates}
                url: {self.url}
                description: {self.description}"""

class Image(db.Model):
    """Images of a park"""

    __tablename__ = "images"

    image_id = db.Column(db.Integer,
                primary_key = True,
                autoincrement = True,
                nullable = False)
    fullname = db.Column(db.Integer,
                db.ForeignKey("parks.fullname"),
                nullable = False)
    url = db.Column(db.String,
                unique = True,
                nullable = False)
    
    park = db.relationship('Park', backref='images')

    def __repr__(self):
        return f"""Image image_id: {self.image_id} 
                fullname: {self.fullname}
                url: {self.url}
                park: {self.park}"""


class UserFavorite(db.Model):
    """A list of user's favorites"""

    __tablename__ = "favorites"

    favorite_id = db.Column(db.Integer,
                primary_key = True,
                autoincrement = True,
                nullable = False)
    fullname = db.Column(db.Integer,
                db.ForeignKey("parks.fullname"),
                nullable = False)
    user_id = db.Column(db.Integer,
                db.ForeignKey("users.user_id"),
                nullable = False)
    is_favorite = db.Column(db.Boolean)

    def __repr__(self):
        return f"""Favorite favorite_id: {self.favorite_id} 
                fullname: {self.fullname}
                user_id: {self.user_id}
                is_favorite: {self.is_favorite}"""

    park = db.relationship('Park', backref='favorites')
    user = db.relationship('User', backref='favorites')


class Topic(db.Model):
    """A list of parks' topics"""

    __tablename__ = "topics"


    topic_id = db.Column(db.Integer,
                primary_key = True,
                autoincrement = True,
                nullable = False)
    topic_name = db.Column(db.String,
                unique = True,
                nullable = False)
    fullname = db.Column(db.Integer,
                db.ForeignKey("parks.fullname"),
                nullable = False)
    user_id = db.Column(db.Integer,
                db.ForeignKey("users.user_id"))
    
    park = db.relationship('Park', backref='topics')
    user = db.relationship('User', backref='topics')
    

    def __repr__(self):
        return f"""Topic topic_id: {self.topic_id} 
                topic_name: {self.topic_name}
                fullname: {self.fullname}
                user_id: {self.user_id}"""



if __name__ == '__main__':
    from server import app

    connect_to_db(app)


"""
TODO:
Change park_name to fullname to match results from API?
"""