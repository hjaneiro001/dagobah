from app.exceptions.baseException import BaseException

class CompanyAlreadyExistsException(BaseException):
    def __init__(self):
        super().__init__()
        self.message = "Company already exist"
        self.statusCode = 404
