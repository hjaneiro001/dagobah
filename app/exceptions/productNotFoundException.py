from app.exceptions.baseException import BaseException

class ProductNotFoundException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "Product not found"
        self.statusCode = 404
