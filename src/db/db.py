import contextlib
from os import environ, listdir
from typing import Generator

import psycopg
import psycopg_pool
from psycopg.errors import DuplicateObject
from psycopg.types.enum import EnumInfo, register_enum

from util.card import CardType

def configure_conn(conn: psycopg.Connection) -> None:
    try:
        info = EnumInfo.fetch(conn, 'card_type')
        register_enum(info, conn, CardType)
    except TypeError:
        print("Could not register card_type enum (a single one of these messages is expected)")

@contextlib.contextmanager
def db_cursor() -> Generator[psycopg.cursor.Cursor, None, None]:
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

def execute_file(filename: str) -> None:
    if filename.endswith(".sql"):
            with db_cursor() as cur:
                try:
                    cur.execute(open(filename,'r').read())
                except DuplicateObject:
                    print('ignoring dup obj error')

def setup() -> None:
    for filename in listdir("src/db/sql/enums/"):
        execute_file(f"src/db/sql/enums/{filename}") 
    for filename in listdir("src/db/sql/setup/"):
        execute_file(f"src/db/sql/setup/{filename}")


dbpool = psycopg_pool.ConnectionPool(
    conninfo=environ.get('psql_connection_string') or
        'postgresql://people_collection:people_collection@postgresdb/people_collection',
    configure=configure_conn
)
