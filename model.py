"""Models for MediocreBand app"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A MediocreBand User"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(15), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(20))

    liked_songs = db.relationship('LikedSongs', backref='user')

    def __repr__(self):
        return f'<User user_id={self.user_id} name={self.fname} {self.lname}>'


class Song(db.Model):
    """A song"""

    __tablename__ = "songs"

    song_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f'<Song title={self.title} author={self.author}>'


class LikedSongs(db.Model):
    """A user's liked songs"""

    __tablename__ = "liked_songs"

    liked_songs_list_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    song_id = db.Column(db.Integer, db.ForeignKey('songs.song_id'))

    song = db.relationship('Song', backref='liked_song')
    user = db.relationship('User', backref="liked_song")

    def __repr__(self):
        return f'<LikedSong user_id={self.user_id} song_id={self.song_id}>'



def connect_to_db(app, db_uri='postgresql:///mediocre'):
    """Connect to database"""

    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from server import app

    connect_to_db(app)