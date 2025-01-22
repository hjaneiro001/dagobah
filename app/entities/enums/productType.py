from enum import Enum

class ProductType(Enum):
    PRODUCTO = ['PRODUCTO',1]
    SERVICIO = ['SERVICIO',2]

    def get_product_type(value):
        for item in ProductType:
            if value in item.value:
                return item
        return None

    def get_type(self):
        return self.value[0]

    def get_value(self):
        return self.value[1]






