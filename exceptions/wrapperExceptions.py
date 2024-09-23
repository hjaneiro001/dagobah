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
        except Exception as e:
            print(e)
            return jsonify({"error": "An internal server error occurred"}), 500

    wrapper.__name__ = f"{f.__name__}_wrapper"
    return wrapper
