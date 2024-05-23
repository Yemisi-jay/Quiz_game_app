from flask import Flask
from app.routes import main

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    return app
