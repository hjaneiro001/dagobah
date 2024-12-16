from enum import Enum

class ProductIva(Enum):
    I27 = ['IVA 27%',0.27,5]
    I21  = ['IVA 21%',21,5]
    I105 = ['IVA 10.5%', 0.105,4]
    I5 = ['IVA 5%', 0.05,5]
    I2C5 = ['IVA 2.5%', 0.025, 5]
    EXENTO = ['IVA EXENTO', 0, 5]
    NOGRAV = ['IVA NO GRAVADO', 0, 5]

    def get_product_iva(value):
        for item in ProductIva:
            if value in item.value:
                return item
        return None

    def get_iva(self):
        return self.value[0]

    def get_value(self):
        return self.value[1]

    def get_code(self):
        return self.value[2]





