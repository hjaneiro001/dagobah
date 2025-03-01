from app.exceptions.baseException import BaseException

class KeyNotFoundException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "Key not found"
        self.statusCode = 404
