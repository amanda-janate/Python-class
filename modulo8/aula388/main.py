import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB = ROOT / DB_NAME
TABLE_NAME = 'customers'

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

# Input de dados na tabela
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight) '
    'VALUES (NULL, "Valdenice Margarida", 70), (NULL, "Edson Henrique", 100)'
)
con.commit()

cursor.close()
con.close()
