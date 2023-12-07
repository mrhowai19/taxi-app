import sqlite3
from sqlite3 import SQLITE_ERROR, Connection
from schemas import *

tables = [CUSTOMER_TABLE, DRIVER_TABLE, ADMIN_TABLE, BOOKING_TABLE]


def create_tables(file: str = 'database.db') -> None:
    conn: Connection or None = None
    try:
        conn = sqlite3.connect(file)
        cur = conn.cursor()
        for table in tables:
            cur.execute(table)
    except Exception as se:
        print(se)
    finally:
        conn.close()


