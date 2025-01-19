from app.exceptions.baseException import BaseException

class CertificateNotFoundException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "Certificate not found"
        self.statusCode = 404
