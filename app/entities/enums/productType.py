from enum import Enum

class ProductType(Enum):
    PRODUCTO = ['PRODUCTO']
    SERVICIO = ['SERVICIO']

    @classmethod
    def get_name(cls, value):
        for item in cls:
            if value == item.value[0]:
                return item.name

    def get_productType(self):
        return self.value[0]





