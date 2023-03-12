from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)

# Flask-SQLAlchemy configuration keys. See: https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
# TODO: Store creds as environment variable
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://root:p%40ssw0rd!@localhost:3306/todoist-clone"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

CORS(app)