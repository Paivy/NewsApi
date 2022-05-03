from ensurepip import bootstrap
from flask import Flask
from app.requests import configure_request
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap

def create_app(config_name):
    app = flask(__name__)
    #Creating the app configurations
    app.config.from_object(config_options[config_name])

    #Initializing flask extensions
    bootstrap.init_app(app)
    #Registering the blueprints
    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    #setting config
    configure_request(app)

    return app
