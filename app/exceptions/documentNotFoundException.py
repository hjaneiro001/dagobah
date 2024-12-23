from app.exceptions.baseException import BaseException

class DocumentNotFoundException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "Document not found"
        self.statusCode = 404
