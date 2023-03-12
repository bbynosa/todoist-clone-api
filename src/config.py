from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_cors import CORS
from flask_migrate import Migrate
import urllib.parse
import logging

password = urllib.parse.quote_plus("j%Y9%E8t5nE$U9")

app = Flask(__name__)


# Flask-SQLAlchemy configuration keys. See: https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
# TODO: Store creds as environment variable
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"mysql+pymysql://flask-api:{password}@192.168.21.10:3306/todoist-clone"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

CORS(app)

logging.getLogger('flask_cors').level = logging.DEBUG