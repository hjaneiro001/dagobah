from flask import Flask

from app.controllers.clientsControllers import clientsBp
from app.controllers.companyController import companyBp
from app.controllers.productsController import productsBp
from app.controllers.documentsController import documentsBp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(clientsBp, url_prefix='/clients')
    app.register_blueprint(productsBp, url_prefix='/products')
    app.register_blueprint(documentsBp, url_prefix='/documents')
    app.register_blueprint(companyBp, url_prefix='/company')

    return app