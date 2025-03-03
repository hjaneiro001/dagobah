import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from flask_cors import CORS


from controllers.clientsControllers import clientsBp
from controllers.companyController import companyBp
from controllers.productsController import productsBp
from controllers.documentsController import documentsBp


def create_app():
    app = Flask(__name__)

    CORS(app, resources={
        r"/*": {
            "origins": "http://127.0.0.1:5500",
            "methods": ["GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })

    app.register_blueprint(clientsBp, url_prefix='/clients')
    app.register_blueprint(productsBp, url_prefix='/products')
    app.register_blueprint(documentsBp, url_prefix='/documents')
    app.register_blueprint(companyBp, url_prefix='/company')

    return app


if __name__ == '__main__':
    create_app().run(host="0.0.0.0", port=5000, debug=False)