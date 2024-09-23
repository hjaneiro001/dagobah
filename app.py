from flask import Flask
from controllers.clientsControllers import clientsBp

app = Flask(__name__)

# Registro del Blueprint
app.register_blueprint(clientsBp, url_prefix='/clients')

if __name__ == '__main__':
    app.run(debug=True)

