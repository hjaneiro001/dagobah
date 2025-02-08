from app.exceptions.validationError import  ValidationError

class ItemValidationException(ValidationError):
    def __init__(self):
        super().__init__()
        self.message = "Error en los Items o Items Nulo"
        self.statusCode = 404
