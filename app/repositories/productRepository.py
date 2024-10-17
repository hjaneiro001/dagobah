
import pymysql.cursors
from app.entities.enums.currency import Currency
from app.entities.enums.productIva import ProductIva
from app.entities.enums.productType import ProductType
from app.entities.enums.status import Status
from app.entities.product import ProductBuilder, Product

class ProductRepository:

    def __init__(self, connection):
        self.conn = connection

    def get_all(self):

            sql = f"SELECT * FROM Products WHERE product_status = '{Status.ACTIVE.value}'"
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
                        .status(Status(row.get('product_status')))
                        .build())

                products.append(product)

            return products

    def get_id(self, id: int):

        sql :str = f"SELECT * FROM products WHERE product_id = %s AND product_status = '{Status.ACTIVE.value}'"
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, (id,))
        row = cursor.fetchone()

        if row is None:
            return None

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
                    .status(Status(row.get('product_status')))
                    .currency(Currency(row.get('product_currency')))
                    .build())

        return product

    def create(self, product: Product):
        sql: str = """
            INSERT INTO products (product_code, product_bar_code, product_name, product_description, product_pack, product_price, product_currency, product_iva, product_type, product_status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            product.code, product.bar_code, product.name, product.description, product.pack,
            product.price, product.currency.value, product.iva.value,
            product.product_type.value, product.status.value
        )

        cursor = self.conn.cursor()
        cursor.execute(sql, values)

        product_id = cursor.lastrowid

        self.conn.commit()

        return product_id

    def find_by_code(self, product_code: str):
        sql: str = f"SELECT * FROM products WHERE product_code = %s AND product_status = '{Status.ACTIVE.value}'"
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, (product_code,))
        row = cursor.fetchone()
        return row

    def save(self, product: Product):
        sql: str = """
            UPDATE products
            SET product_code = %s, product_name = %s, product_description = %s, product_bar_code = %s, product_pack = %s, 
                product_price = %s, product_currency = %s, product_iva = %s, product_type = %s, 
                product_status = %s
            WHERE product_id = %s
        """

        values = (
            product.code, product.name, product.description, product.bar_code, product.pack, product.price,
            product.currency.value, product.iva.value, product.product_type.value, product.status.value,
            product.product_id
        )

        cursor = self.conn.cursor()
        cursor.execute(sql, values)
        self.conn.commit()
        cursor.close()
