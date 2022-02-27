from flask import Flask
from os import getenv
from app.configs import database, migrations
from app import routes
from app.services.populate_table import populate_table


def create_app() -> Flask:
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False

    database.init_app(app)
    migrations.init_app(app)

    routes.init_app(app)

    return app
