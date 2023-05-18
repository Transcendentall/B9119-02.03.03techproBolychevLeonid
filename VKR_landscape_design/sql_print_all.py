import sqlite3
import pandas as pd
import numpy as np
from models.animals_model import *
from models.grounds_model import *
from models.plants_model import *
from models.soils_model import *
from models.territories_model import *
from models.users_model import *
from models.connection_territories_soils_model import *
from models.connection_soils_grounds_model import *
from models.connection_soils_plants_model import *
from models.connection_plants_animals_model import *
pd.options.display.max_rows = 100
pd.options.display.max_columns = 100

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


cursor.execute("SELECT * FROM connection_plants_animals")
print(cursor.fetchall())

print()





print()
print('--------------------')
print()

#print(get_plants(con))
#insert_plant(con, 'qqq', 'www', 'eee')
#delete_plant(con, 6)
#update_plant_name(con, 7, 'IVAN!')
#print(get_plants(con))

print(get_one_user(con, 1))
print(get_one_user_without_password(con, 1))
print(authorisation(con, 'lutiysidor', 'abracadabra123'))

print(get_animals_for_plant(con, 4))
print(bycoord(con, 43.10562, 131.87353))