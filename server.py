"""Server for MediocreBand app"""

from flask import Flask, render_template, jsonify
from model import connect_to_db
import crud

app = Flask(__name__)
app.secret_key = "dev"

@app.route('/')
def render_homepage():
    """Renders MediocreBand homepage"""

    return render_template('homepage.html')


@app.route('/songs')
def show_all_songs():
    """Returns all Songs in database"""
    fake_song_dict = [{'title': 'Firework', 'author': 'Katy Perry'},
                        {'title': 'Dancing With The Devil', 'author': 'Demi Lovato'}]

    return jsonify(fake_song_dict)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, use_reloader=True, use_debugger=True)