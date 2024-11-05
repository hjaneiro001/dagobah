from app.exceptions.baseException import BaseException

class ClientTaxIdAlreadyExistsException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "The tax Id already exists"
        self.statusCode = 409
