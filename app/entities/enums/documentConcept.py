from enum import Enum

class DocumentConcept(Enum):
    PR = ['PRODUCTOS', 1]
    SE = ['SERVICIOS', 2]
    PS = ['PRODUCTOS Y SERVICIOS', 3]

    def get_document_concept(value):
        for item in DocumentConcept:
            if value in item.value:
                return item
        return None

    def get_concept(self):
        return self.value[0]

    def get_value(self):
        return self.value[1]
