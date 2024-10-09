import traceback

import pymysql
from flask import jsonify
from marshmallow import ValidationError
from exceptions.baseException import BaseException


def handle_exceptions(f):
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except BaseException as e:
            return jsonify({"error": e.getMessage()}), e.getCode()
        except ValidationError as err:
            print(err)
            message = list(err.messages.values())[0][0]
            return jsonify({"error": message}), 400
        except ValueError as e:
            print("Error: An error ocurred when convert enum")
            return jsonify({"error": "An enum convert error"}), 500
        except pymysql.MySQLError as e:
            print(e)
            print("Error: An error ocurred when we use database")
            return jsonify({"error": "An internal server error occurred"}), 500
        except Exception as e:
            print(traceback.format_exception())
            return jsonify({"error": "An internal server error occurred"}), 500

    wrapper.__name__ = f"{f.__name__}_wrapper"
    return wrapper
