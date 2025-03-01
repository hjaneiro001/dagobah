from app.exceptions.baseException import BaseException

class DocumentAlreadyExistsException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "The document already exists"
        self.statusCode = 409
