from enum import Enum

from app.entities.enums.productIva import ProductIva


class ProductType(Enum):
    PRODUCTO = ['PRODUCTO']
    SERVICIO = ['SERVICIO']

    #  @classmethod
    def get_product_type(value):
        for item in ProductType:
            if value in item.value:
                return item
        return None

    def get_type(self):
        return self.value[0]

    # @classmethod
    # def get_name(cls, value):
    #     for item in cls:
    #         if value == item.value[0]:
    #             return item.name
    #
    # def get_productType(self):
    #     return self.value[0]





