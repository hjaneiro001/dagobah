from app.exceptions.validationError import  ValidationError

class DocumentTypeForbidenException(ValidationError):
    def __init__(self):
        super().__init__()
        self.message = "Document Type forbiden"
        self.statusCode = 404
