import os

import psycopg2
from dotenv import load_dotenv
from psycopg2 import sql

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")

conn = psycopg2.connect(
    host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD, port=DB_PORT
)


def create_table(table_name, columns: dict):
    """
    Dynamische, sichere Tabellenerstellung
    columns: dict, z.B. {"id": "SERIAL PRIMARY KEY", "title": "TEXT"}
    """
    allowed_types = ["TEXT", "BOOLEAN", "INT", "SERIAL", "DATE", "TIMESTAMP"]
    cols = []
    for name, dtype in columns.items():
        if any(t in dtype.upper() for t in allowed_types):
            cols.append(sql.SQL("{} {}").format(sql.Identifier(name), sql.SQL(dtype)))
        else:
            raise ValueError(f"Datentyp {dtype} nicht erlaubt")

    cursor = conn.cursor()
    query = sql.SQL("CREATE TABLE IF NOT EXISTS {} ({});").format(
        sql.Identifier(table_name), sql.SQL(", ").join(cols)
    )
    cursor.execute(query)
    conn.commit()
    cursor.close()


# Beispiel-Tabelle
create_table(
    "tasks",
    {
        "id": "SERIAL PRIMARY KEY",
        "title": "TEXT NOT NULL",
        "description": "TEXT",
        "completed": "BOOLEAN DEFAULT FALSE",
        "due_date": "DATE",
        "created_at": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
    },
)
