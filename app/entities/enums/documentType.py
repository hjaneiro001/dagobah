from enum import Enum

class DocumentType(Enum):
    FACTURAA = ['FACTURAA', 1,'A']
    NOTADECREDITOA = ['NOTA DE CREDITOA', 2,'A']
    NOTADEDEBITOA = ['NOTA DE DEBITOA', 3,'A']
    RECIBOA = ['RECIBOA', 4, 'A']
    FACTURAB = ['FACTURAB', 5, 'B']
    NOTADECREDITOB = ['NOTA DE CREDITOB', 6, 'B']
    NOTADEDEBITOB = ['NOTA DE DEBITOB', 7, 'B']
    RECIBOB = ['RECIBOB', 8, 'B']
    FACTURAC = ['FACTURAC', 11, 'C']
    NOTADECREDITOC = ['NOTA DE CREDITOC', 12, 'C']
    NOTADEDEBITOC = ['NOTA DE DEBITOC', 13, 'C']
    RECIBOC = ['RECIBOC', 14, 'C']

    def get_document_type( value):
        for item in DocumentType:
            if value in item.value:
                return item
        return None

    def get_type(self):
        return self.value[0]

    def get_value(self):
        return self.value[1]

    def get_letra(self):
        return self.value[2]

