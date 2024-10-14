from app.entities.enums.clientStatus import ClientStatus
from app.entities.enums.currency import Currency
from app.entities.enums.productIva import ProductIva
from app.entities.enums.productType import ProductType
from app.entities.product import ProductBuilder, Product

class ProductRepository:

    def __init__(self, connection):
        self.conn = connection

    def get_all(self):
        product1 = (
            ProductBuilder()
            .product_id(1)
            .code("ProductCode")
            .bar_code("BarCode")
            .name("FAKE Product")
            .description("Description")
            .pack(1)
            .price(1)
            .currency(Currency.ARS)
            .iva(ProductIva.I21)
            .product_type(ProductType.BC)
            .status(ClientStatus.ACTIVE)
            .build()
        )

        product2 = (
            ProductBuilder()
            .product_id(2)
            .code("ProductCode2")
            .bar_code("BarCode2")
            .name("FAKE Product 2")
            .description("Description 2")
            .pack(2)
            .price(2)
            .currency(Currency.ARS)
            .iva(ProductIva.I21)
            .product_type(ProductType.BC)
            .status(ClientStatus.ACTIVE)
            .build()
        )

        return [product1, product2]


