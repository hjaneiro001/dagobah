
import pymysql.cursors
from app.entities.enums.currency import Currency
from app.entities.enums.productIva import ProductIva
from app.entities.enums.productType import ProductType
from app.entities.enums.clientStatus import ClientStatus
from app.entities.product import ProductBuilder, Product

class ProductRepository:

    def __init__(self, connection):
        self.conn = connection

    # def get_all(self):
    #     product1 = (
    #         ProductBuilder()
    #         .product_id(1)
    #         .code("ProductCode")
    #         .bar_code("BarCode")
    #         .name("FAKE Product")
    #         .description("Description")
    #         .pack(1)
    #         .price(1)
    #         .currency(Currency.ARS)
    #         .iva(ProductIva.I21)
    #         .product_type(ProductType.BC)
    #         .status(ClientStatus.ACTIVE)
    #         .build()
    #     )
    #
    #     product2 = (
    #         ProductBuilder()
    #         .product_id(2)
    #         .code("ProductCode2")
    #         .bar_code("BarCode2")
    #         .name("FAKE Product 2")
    #         .description("Description 2")
    #         .pack(2)
    #         .price(2)
    #         .currency(Currency.ARS)
    #         .iva(ProductIva.I21)
    #         .product_type(ProductType.BC)
    #         .status(ClientStatus.ACTIVE)
    #         .build()
    #     )
    #
    #     return [product1, product2]
    #

    def get_all(self):

            sql = "SELECT * FROM Products WHERE product_status = 'ACTIVE'"
            cursor = self.conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            rows = cursor.fetchall()

            products:  list[Product] = []

            for row in rows:
                product = (ProductBuilder()
                        .product_id(row.get('product_id'))
                        .code(row.get('product_code'))
                        .bar_code(row.get('product_bar_code'))
                        .name(row.get('product_name'))
                        .description(row.get('product_description'))
                        .pack(row.get('product_pack'))
                        .price(row.get('product_price'))
                        .currency(Currency(row.get('product_currency')))
                        .iva(ProductIva(row.get('product_iva')))
                        .product_type(ProductType(row.get('product_type')))
                        .status(ClientStatus(row.get('product_status')))
                        .build())

                products.append(product)

            return products

