import contextlib
import os
from os import environ, listdir
from typing import Generator

import psycopg
import psycopg_pool

dbpool = psycopg_pool.ConnectionPool(
    conninfo=environ.get('psql_connection_string') or
             'postgresql://people_collection:people_collection@postgresdb/people_collection'
)

@contextlib.contextmanager
def db_cursor () -> Generator[psycopg.cursor.Cursor, None, None]:
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
    for filename in listdir("src/db/sql/setup/"):
        if filename.endswith(".sql"):
            with db_cursor() as cur:
                cur.execute( open( f"src/db/sql/setup/{filename}",'r').read())
