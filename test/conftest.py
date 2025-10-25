from typing import Generator

import pytest
import psycopg2
import time 
import os

from utils import config


@pytest.fixture(scope="session")
def db_connection() -> Generator[None, None, psycopg2.extensions.connection]:
    for _ in range(10):
        try:
            conn = psycopg2.connect(
                database=config.DATABASE_URL,
                user=config.DATABASE_USER,
                password=config.DATABASE_PASSWORD
            )
            break
        except psycopg2.OperationalError:
            time.sleep(5)
    else:
        raise RuntimeError("Could not connect to the database")
    
    yield conn
    conn.close()


@pytest.fixture(scope="session")
def cursor(db_conn: psycopg2.extensions.connection):
    cur = db_conn.cursor()
    yield cur
    db_conn.rollback()
    cur.close()