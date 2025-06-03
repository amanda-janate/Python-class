import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB = ROOT / DB_NAME
TABLE_NAME = 'customers'

if __name__ == '__main__':
    con = sqlite3.connect(DB)
    cursor = con.cursor()

    # Criar tabela
    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
        '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT, '
        'name TEXT,'
        'weight REAL'
        ')'
    )
    con.commit()

    # limpar a tabela
    cursor.execute(
        f'DELETE FROM {TABLE_NAME}'
    )
    # Zerar ids
    cursor.execute(
        f'DELETE FROM sqlite_sequence WHERE name = "{TABLE_NAME}"'
    )
    con.commit()

    sql = (f'INSERT INTO {TABLE_NAME} (name, weight) '
        'VALUES (:nome, :peso)')
    # Input de dados na tabela
    # cursor.execute(sql, ['Valdenice Margarida', 70])
    # cursor.executemany(
    #     sql,
    #     (('Valdenice Margarida', 70),
    #     ('Edson', 34))
    # )
    cursor.execute(sql, {'nome':'Edson','peso': 34})

    cursor.executemany(
        sql,
        (
            {'nome':'Val','peso': 75},
            {'nome':'Amanda','peso': 90},
            {'nome':'Helena','peso': 56},
            {'nome':'Jair','peso': 120},
        )
    )

    con.commit()

    cursor.close()
    con.close()
