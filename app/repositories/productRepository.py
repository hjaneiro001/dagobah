
import pymysql.cursors
from sqlalchemy import QueuePool

from app.entities.enums.currency import Currency
from app.entities.enums.productIva import ProductIva
from app.entities.enums.productType import ProductType
from app.entities.enums.status import Status
from app.entities.product import ProductBuilder, Product
from app.utils.connection_manager import ConnectionManager
from app.utils.cursor_manager import CursorManager


class ProductRepository:

    def __init__(self, pool_connection: QueuePool):
        self.pool_connection: QueuePool = pool_connection

    def get_all(self):

        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:

                sql = f"SELECT * FROM PRODUCTS WHERE product_status = '{Status.ACTIVE.get_value()}'"

                cur.execute(sql)
                rows = cur.fetchall()

                products:  list[Product] = []

                for row in rows:
                    product = (ProductBuilder()
                            .product_id(row.get('product_id'))
                            .code(row.get('product_code'))
                            .name(row.get('product_name'))
                            .description(row.get('product_description'))
                            .price(row.get('product_price'))
                            .currency(Currency.get_currency(row.get('product_currency')))
                            .iva(ProductIva.get_product_iva(row.get('product_iva')))
                            .product_type(ProductType.get_product_type(row.get('product_type')))
                            .status(Status.get_status(row.get('product_status')))
                            .build())

                    products.append(product)


            return products

    def get_id(self, id: int):

        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:

                sql :str = f"SELECT * FROM PRODUCTS WHERE product_id = %s AND product_status = '{Status.ACTIVE.get_value()}'"

                cur.execute(sql, (id,))
                row = cur.fetchone()

                if row is None:
                    return None

                product = (ProductBuilder()
                            .product_id(row.get('product_id'))
                            .code(row.get('product_code'))
                            .name(row.get('product_name'))
                            .description(row.get('product_description'))
                            .price(row.get('product_price'))
                            .currency(Currency.get_currency(row.get('product_currency')))
                            .iva(ProductIva.get_product_iva(row.get('product_iva')))
                            .product_type(ProductType.get_product_type(row.get('product_type')))
                            .status(Status.get_status(row.get('product_status')))
                            .build())

                cur.close()

                return product

    def create(self, product: Product):

        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:

                sql: str = """
                    INSERT INTO PRODUCTS (product_code, product_name, product_description, product_price, product_currency, product_iva, product_type, product_status)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """

                values = (
                    product.code, product.name, product.description,
                    product.price,product.currency.get_value() , product.iva.get_iva(),
                    product.product_type.get_type(), product.status.get_value()
                )

                cur.execute(sql, values)

                product_id = cur.lastrowid

                conn.commit()

                return product_id

    def find_by_code(self, product_code: str):

        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:

                sql: str = f"SELECT * FROM PRODUCTS WHERE product_code = %s AND product_status = '{Status.ACTIVE.get_value()}'"

                cur.execute(sql, (product_code,))
                row = cur.fetchone()

                if row is None:
                    return None

                product = (ProductBuilder()
                           .product_id(row.get('product_id'))
                           .code(row.get('product_code'))
                           .name(row.get('product_name'))
                           .description(row.get('product_description'))
                           .price(row.get('product_price'))
                           .currency(Currency.get_currency(row.get('product_currency')))
                           .iva(ProductIva.get_product_iva(row.get('product_iva')))
                           .product_type(ProductType.get_product_type(row.get('product_type')))
                           .status(Status.get_status(row.get('product_status')))
                           .build())

                cur.close()
                conn.close()

                return product


    def save(self, product: Product):

        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:

                sql: str = """
                    UPDATE PRODUCTS
                    SET product_code = %s, product_name = %s, product_description = %s, 
                        product_price = %s, product_currency = %s, product_iva = %s, product_type = %s,
                        product_status = %s
                    WHERE product_id = %s
                """

                values = (
                    product.code, product.name, product.description,
                    product.price, product.currency.get_value() ,
                    product.iva.get_iva(), product.product_type.get_type(), product.status.get_value(),
                    product.product_id
                )

                cur.execute(sql, values)
                conn.commit()
                cur.close()
                conn.close()

    def get_by_list(self, list_product):
        if not list_product:
            return []

        placeholders = ', '.join(['%s'] * len(list_product))

        sql = f"""
            SELECT * 
            FROM PRODUCTS 
            WHERE product_id IN ({placeholders}) 
              AND product_status = %s
        """

        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:

                params = list_product + [Status.ACTIVE.get_value()]
                cur.execute(sql, params)
                rows = cur.fetchall()

                products = [
                    ProductBuilder()
                    .product_id(row.get('product_id'))
                    .code(row.get('product_code'))
                    .name(row.get('product_name'))
                    .description(row.get('product_description'))
                    .price(row.get('product_price'))
                    .currency(Currency.get_currency(row.get('product_currency')))
                    .iva(ProductIva.get_product_iva(row.get('product_iva')))
                    .product_type(ProductType.get_product_type(row.get('product_type')))
                    .status(Status.get_status(row.get('product_status')))
                    .build()
                    for row in rows
                ]

                return products





