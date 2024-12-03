from typing import List

from sqlalchemy import QueuePool

from app.entities.enums.status import Status
from app.entities.item import Item
from app.utils.connection_manager import ConnectionManager
from app.utils.cursor_manager import CursorManager


class ItemRepository:

    def __init__(self, pool_connection: QueuePool):
        self.pool_connection: QueuePool = pool_connection

    def create(self, item: Item, document_id :int):

        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:

                sql: str = """
                      INSERT INTO items (document_id,product_id, quantity, tax_rate,unit_price,status) VALUES (%s,%s,%s,%s,%s) 
                      """

                values = (document_id, item.product_id, item.quantity,item.tax_rate,item.unit_price,Status.ACTIVE.get_value())

                cur.execute(sql,values)
                conn.commit()

