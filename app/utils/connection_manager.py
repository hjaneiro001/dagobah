from pymysql import Connection
from pymysql.cursors import Cursor
from sqlalchemy import QueuePool


class ConnectionManager:

    def __init__(self, pool: QueuePool):
        self.pool: QueuePool = pool
        self.conn: Connection = None

    def __enter__(self):
        self.conn = self.pool.connect()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
