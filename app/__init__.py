from flask import Flask

from app.controllers.clientsControllers import clientsBp
from app.controllers.productsController import productsBp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(clientsBp, url_prefix='/clients')
    app.register_blueprint(productsBp, url_prefix='/products')

    return app