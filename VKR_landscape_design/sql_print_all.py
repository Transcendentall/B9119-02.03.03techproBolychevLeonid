import sqlite3
import pandas as pd

# PRAGMA FOREIGN_KEYS = on;

con = sqlite3.connect("VKR.sqlite")
con.commit()

cursor = con.cursor()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
cursor.execute("SELECT * FROM territories")
print(cursor.fetchall())
cursor.execute("SELECT * FROM soils")
print(cursor.fetchall())
cursor.execute("SELECT * FROM animals")
print(cursor.fetchall())
cursor.execute("SELECT * FROM plants")
print(cursor.fetchall())
cursor.execute("SELECT * FROM grounds")
print(cursor.fetchall())
cursor.execute("SELECT * FROM connection_territories_soils")
print(cursor.fetchall())
cursor.execute("SELECT * FROM connection_soils_grounds")
print(cursor.fetchall())
cursor.execute("SELECT * FROM connection_soils_plants")
print(cursor.fetchall())
cursor.execute("SELECT * FROM connection_plants_animals")
print(cursor.fetchall())

print()