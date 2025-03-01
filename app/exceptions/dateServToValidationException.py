from app.exceptions.validationError import  ValidationError

class DateServToValidationException(ValidationError):
    def __init__(self):
        super().__init__()
        self.message = "El valor de la fecha hasta deberia ser mayor al valor de la fecha desde"
        self.statusCode = 404
