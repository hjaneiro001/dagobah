from app.exceptions.validationError import  ValidationError

class CurrencySetNotValidException(ValidationError):
    def __init__(self):
        super().__init__()
        self.message = "Several Currencies not valid"
        self.statusCode = 404
