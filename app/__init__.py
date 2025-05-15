from flask import Flask
import os

def create_app():
    # Tell Flask explicitly where to find templates
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))

    from .routes import main
    app.register_blueprint(main)

    return app
