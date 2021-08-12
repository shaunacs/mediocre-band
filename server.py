"""Server for MediocreBand app"""

from flask import Flask
from model import connect_to_db

app = Flask(__name__)
app.secret_key = "dev"