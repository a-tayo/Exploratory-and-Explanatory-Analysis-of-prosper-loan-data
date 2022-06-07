import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
username = 'u0_a222'
password = ''
url = 'localhost:5432'
DATABASE_NAME = 'fyyur'

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = f'postgresql://{username}:{password}@{url}/{DATABASE_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False