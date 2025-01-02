import contextlib
from os import environ, listdir
from typing import Generator

import psycopg2.pool
from psycopg2.extensions import cursor

dbpool = psycopg2.pool.ThreadedConnectionPool(
    host=       environ.get("") or "127.0.0.1",
    port=       environ.get("") or "5432",
    user=       environ.get("") or "people_collection",
    password=   environ.get("") or "people_collection",
    minconn=1,
    maxconn=5
)

@contextlib.contextmanager
def db_cursor () -> Generator[cursor, None, None]:
    conn = dbpool.getconn()
    try:
        with conn.cursor() as cur:
            yield cur
            conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        dbpool.putconn(conn)

def setup ():
    for filename in listdir("sql/setup/"):
        if filename.endswith(".sql"):
            with db_cursor() as cur:
                cur.execute( open( f"sql/setup/{filename}",'r').read())
