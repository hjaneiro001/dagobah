from app.entities.product import Product, ProductBuilder
from app.entities.enums.clientStatus import ClientStatus
from app.entities.enums.productType import  ProductType
from app.entities.enums.productIva import ProductIva
from app.entities.enums.currency import Currency

class ProductMother:
    @staticmethod
    def normal_product(product_id: int):
        product: Product = (ProductBuilder()
                            .product_id(product_id)
                            .code("P001")
                            .bar_code("1234567890123")
                            .name("Sample Product")
                            .description("This is a sample product.")
                            .pack(1.0)
                            .price(9.99)
                            .currency(Currency.ARS)
                            .iva(ProductIva.I21)
                            .product_type(ProductType.PRODUCTO)
                            .status(ClientStatus.ACTIVE)
                            .build())
        return product