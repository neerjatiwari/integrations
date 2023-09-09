# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from app import app



app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app import routes

