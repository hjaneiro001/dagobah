from enum import Enum

class DocumentType(Enum):
    FACTURAA = ['FACTURAA', 1,'A','FACTURA']
    NOTADECREDITOA = ['NOTA DE CREDITOA', 2,'A','NOTA DE CREDITO']
    NOTADEDEBITOA = ['NOTA DE DEBITOA', 3,'A','NOTA DE DEBITO']
    RECIBOA = ['RECIBOA', 4, 'A','RECIBO']
    FACTURAB = ['FACTURAB', 5, 'B','FACTURA']
    NOTADECREDITOB = ['NOTA DE CREDITOB', 6, 'B','NOTA DE CREDITO']
    NOTADEDEBITOB = ['NOTA DE DEBITOB', 7, 'B','NOTA DE DEBITO']
    RECIBOB = ['RECIBOB', 8, 'B','RECIBO']
    FACTURAC = ['FACTURAC', 11, 'C','FACTURA']
    NOTADECREDITOC = ['NOTA DE CREDITOC', 12, 'C','NOTA DE CREDITO']
    NOTADEDEBITOC = ['NOTA DE DEBITOC', 13, 'C','NOTA DE DEBITO']
    RECIBOC = ['RECIBOC', 14, 'C','RECIBO']

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

    def get_document(self):
        return self.value[3]


