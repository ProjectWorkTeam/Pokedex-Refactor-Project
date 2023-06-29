# import statement for CSRF
#/pokedex-refactor- flask/flask-backend/app/__init__.py
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask import Flask, request, redirect, render_template
from .config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.cli.command("seed_db")
def seed_db():
    from .seeders.pokemon import seed_data
    from .seeders.items import seed_items

    print("Seeding database...")
    seed_data(db)
    seed_items(db)
    print("Database seeding complete!")

@app.route("/")
def home():
    return "<h1>Pokemon Refactor</h1>"

# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response
