from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        "RENDER_DATABASE_URI")
    if os.environ.get(
        "RENDER_DATABASE_URI") == None:
        raise ValueError("la connection string está empty")

    # Register Blueprints here
    # from .routes import example_bp
    # app.register_blueprint(example_bp)
    from app.routes import analytics_bp

    app.register_blueprint(analytics_bp)

    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    return app