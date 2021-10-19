"""MediocreBand CRUD operations"""

from model import db, connect_to_db, User, Song, LikedSong

def create_user(fname, lname, email, username, password):
    """Creates and returns a new user"""

    user = User(fname=fname, lname=lname, email=email,
                username=username, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_song(title, author):
    """Creates and returns a song"""

    song = Song(title=title, author=author)
    db.session.add(song)
    db.session.commit()

    return song


def create_liked_song(user, song):
    """Creates an instance of LikedSong"""

    liked_song = LikedSong(user_id=user.user_id, song_id=song.song_id)
    db.session.add(liked_song)
    db.session.commit()

    return liked_song


def view_all_songs():
    """Returns a list of all songs"""

    return Song.query.all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)