from enum import Enum

class DocumentType(Enum):
    FACTURA = ['FACTURA', 0]
    NOTADECREDITO = ['NOTA DE CREDITO', 1]

    def get_document_type( value):
        for item in DocumentType:
            if value in item.value:
                return item
        return None

    def get_type(self):
        return self.value[0]


    def get_value(self):
        return self.value[1]
