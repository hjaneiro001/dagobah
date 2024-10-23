from enum import Enum

class ClientType(Enum):
    CLIENTE = ['CLIENTE']
    PROVEEDOR = ['PROVEEDOR']
    AMBOS = ['AMBOS']

    def get_clientType(value):
        for item in ClientType:
            if value in item.value:
                return item
        return None

    def get_type(self):
        return self.value[0]