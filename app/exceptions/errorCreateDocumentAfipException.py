from app.exceptions.baseException import BaseException

class ErrorCreateDocumentAfipException(BaseException):
    def __init__(self, ):
        super().__init__()
        self.message = "Document afip coudn't be created"
        self.statusCode = 502

