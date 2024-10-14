
import pymysql.cursors
from app.entities.enums.currency import Currency
from app.entities.enums.productIva import ProductIva
from app.entities.enums.productType import ProductType
from app.entities.enums.clientStatus import ClientStatus
from app.entities.product import ProductBuilder, Product

class ProductRepository:

    def __init__(self, connection):
        self.conn = connection

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

