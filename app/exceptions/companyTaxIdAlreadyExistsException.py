from app.exceptions.baseException import BaseException

class CompanyTaxIdAlreadyExistsException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "The tax Id already exists for this company"
        self.statusCode = 409
