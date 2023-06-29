import os
from flask_sqlalchemy import SQLAlchemy

class Configuration:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Create a SQLAlchemy instance
db = SQLAlchemy()
