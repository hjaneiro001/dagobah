from app.exceptions.baseException import BaseException

class ProductAlreadyExistsException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "The product already exist"
        self.statusCode = 409




