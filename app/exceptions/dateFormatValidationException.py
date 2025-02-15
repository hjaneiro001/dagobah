from app.exceptions.validationError import  ValidationError

class DateFormatValidationException(ValidationError):
    def __init__(self):
        super().__init__()
        self.message = "El formato de fecha deberia ser 'YYYYMMDD'"
        self.statusCode = 404
