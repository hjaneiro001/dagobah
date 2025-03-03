import traceback
import logging
import pymysql
from flask import jsonify
from marshmallow import ValidationError
from app.exceptions.baseException import BaseException
from app.exceptions.validationError import ValidationError

def handle_exceptions(f):

    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except BaseException as e:
            logging.error(traceback.format_exc())
            return jsonify({"error": e.getMessage()}), e.getCode()
        except ValidationError as e:
            logging.error(traceback.format_exc())
            return jsonify({"error": e.getMessage()}), e.getCode()
        except ValueError as e:
            logging.error(traceback.format_exc())
            logging.error("Error: An error ocurred when convert enum")
            return jsonify({"error": "An enum convert error"}), 500
        except pymysql.MySQLError as e:
            logging.error(e)
            logging.error("Error: An error ocurred when we use database")
            return jsonify({"error": "An internal server error occurred"}), 500
        except Exception as e:
            logging.error(e)
            logging.error(traceback.format_exc())
            return jsonify({"error": "An internal server error occurred"}), 500

    wrapper.__name__ = f"{f.__name__}_wrapper"
    return wrapper
