from enum import Enum

class ProductIva(Enum):
    I27 = ['IVA 27%',0.27]
    I21  = ['IVA 21%',0.21]
    I105 = ['IVA 10.5%', 0.105]
    I5 = ['IVA 5%', 0.05]
    I2C5 = ['IVA 2.5%', 0.025]
    EXENTO = ['IVA EXENTO', 0]
    NOGRAV = ['IVA NO GRAVADO', 0]

    def get_product_iva(value):
        for item in ProductIva:
            if value in item.value:
                return item
        return None

    def get_iva(self):
        return self.value[0]

    def get_value(self):
        return self.value[1]





