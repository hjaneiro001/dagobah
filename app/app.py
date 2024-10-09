from flask import Flask
from controllers.clientsControllers import clientsBp
from entities.enums.taxCondition import TaxCondition

app = Flask(__name__)

app.register_blueprint(clientsBp, url_prefix='/clients')

if __name__ == '__main__':
    app.run(debug=True)
