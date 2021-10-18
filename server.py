"""Server for MediocreBand app"""

from flask import Flask, render_template
from model import connect_to_db

app = Flask(__name__)
app.secret_key = "dev"

@app.route('/')
def render_homepage():
    """Renders MediocreBand homepage"""

    return render_template('homepage.html')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, use_reloader=True, use_debugger=True)