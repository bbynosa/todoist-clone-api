from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_cors import CORS
from flask_migrate import Migrate
from os import environ

app = Flask(__name__)

# Flask-SQLAlchemy configuration keys. See: https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
'''
Environment variables for configuration:
MYSQL_USER - username of MySQL database user
MYSQL_PASS - password of MySQL database password
MYSQL_HOST - hostname of MySQL database 
MYSQL_PORT - port number of MySQL database 
'''
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"mysql+pymysql://{environ['MYSQL_USER']}:{environ['MYSQL_PASS']}@{environ['MYSQL_HOST']}:{environ['MYSQL_PORT']}/todoist-clone"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

CORS(app)
