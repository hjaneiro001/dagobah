from pymysql.connections import Connection
from pymysql.cursors import Cursor


class CursorManager:

    def __init__(self, conn: Connection):
        self.conn: Connection = conn
        self.cur: Cursor = None

    def __enter__(self):
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur is not None:
            self.conn.close()