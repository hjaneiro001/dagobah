from app.exceptions.validationError import  ValidationError

class DateExpirationValidationException(ValidationError):
    def __init__(self):
        super().__init__()
        self.message = "El valor de la fecha expiration deberia ser mayor que la fecha de emision"
        self.statusCode = 404
