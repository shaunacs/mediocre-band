"""Script to seed fake database for MediocreBand"""

import os
import model
import server

os.system('dropdb mediocre')
os.system('createdb mediocre')
model.connect_to_db(server.app)
model.db.create_all()