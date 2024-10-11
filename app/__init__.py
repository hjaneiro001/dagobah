from flask import Flask

from app.controllers.clientsControllers import clientsBp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(clientsBp, url_prefix='/clients')

    return app