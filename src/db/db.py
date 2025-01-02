import contextlib
from os import environ, listdir
from typing import Generator

import psycopg
import psycopg_pool

dbpool = psycopg_pool.ConnectionPool(
    conninfo=environ.get('psql_connection_string') or
             'postgresql://people_collection:people_collection@127.0.0.1/people_collection'
)

@contextlib.contextmanager
def db_cursor () -> Generator[psycopg.cursor, None, None]:
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
