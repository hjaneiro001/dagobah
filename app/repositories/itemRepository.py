
from sqlalchemy import QueuePool

from app.entities.enums.productIva import ProductIva
from app.entities.enums.status import Status
from app.entities.item import Item, ItemBuilder
from app.utils.connection_manager import ConnectionManager
from app.utils.cursor_manager import CursorManager

class ItemRepository:

    def __init__(self, pool_connection: QueuePool):
        self.pool_connection: QueuePool = pool_connection

    def create(self, items: list[Item],document_id :int):

         with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:
                sql: str = """
                    INSERT INTO items (document_id, product_id, quantity, tax_rate, unit_price,discount, status)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """

                values = [
                    (
                        document_id,
                        item.product_id,
                        item.quantity,
                        item.tax_rate.get_value(),
                        item.unit_price,
                        item.discount,
                        Status.ACTIVE.get_value()
                    )
                    for item in items
                ]

                cur.executemany(sql, values)

                conn.commit()

    def get_by_document_id(self, id:int):

        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:
                sql = f"SELECT * FROM Items i inner join Products p on i.product_id = p.product_id WHERE  document_id = %s and status = '{Status.ACTIVE.get_value()}'"

                cur.execute(sql, (id))
                rows = cur.fetchall()

                items = []
                for item_data in rows:
                    item :Item = (
                        ItemBuilder()
                        .item_id(item_data["item_id"])
                        .product(item_data["product_id"])
                        .quantity(item_data["quantity"])
                        .unit_price(item_data["unit_price"])
                        .discount(item_data["discount"])
                        .product_name(item_data["product_name"])
                        .product_code(item_data["product_code"])
                        .build()
                    )
                    items.append(item)


            return items











