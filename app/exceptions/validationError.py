class ValidationError(Exception):
    def __init__(self):
        self.message = ""
        self.statusCode = 0

    def getMessage(self):
        return self.message

    def getCode(self):
        return self.statusCode
