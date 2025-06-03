import sqlite3
from main import DB, TABLE_NAME

con = sqlite3.connect(DB)
cursor = con.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

# cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE ID = 3')
# con.commit()

cursor.execute(f'UPDATE {TABLE_NAME} SET NAME="Maria" WHERE ID = 1')
con.commit()

print()
# cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE ID = 5')

# row = cursor.fetchone()
# _id, name, weight = row
# print(row)
# print(_id, name, weight)

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

cursor.close()
con.close()
