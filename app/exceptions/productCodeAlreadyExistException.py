from app.exceptions.baseException import BaseException

class ProductCodeAlreadyExistsException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "The product's code already exist"
        self.statusCode = 409




