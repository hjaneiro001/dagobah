from app.exceptions.baseException import BaseException

class ClientNotFoundException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "Client not found"
        self.statusCode = 404
