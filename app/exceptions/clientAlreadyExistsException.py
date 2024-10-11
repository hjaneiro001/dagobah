from app.exceptions.baseException import BaseException

class ClientAlreadyExistsException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "The client already exists"
        self.statusCode = 409
