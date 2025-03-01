from app.exceptions.validationError import  ValidationError

class DateServValidationException(ValidationError):
    def __init__(self):
        super().__init__()
        self.message = "Para concepto servicio o producto debe contener los camps fecha desde, fecha hasta y fecha Vto"
        self.statusCode = 404
