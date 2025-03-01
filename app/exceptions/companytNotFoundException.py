from app.exceptions.baseException import BaseException

class CompanyNotFoundException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "Company not found"
        self.statusCode = 404
