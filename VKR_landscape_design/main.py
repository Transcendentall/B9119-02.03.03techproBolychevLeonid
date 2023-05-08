import sqlite3
import numpy as np
import pandas as pd
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

con.executescript('''

 ''')



con.commit()

cursor = con.cursor()

print(get_animals(con))
print(get_users(con))
print(get_grounds(con))
print(get_plants(con))
print(get_soils(con))
print(get_territories(con))
print(get_users_without_password(con))
print(get_users_without_password_admins(con))
print(get_users_without_password_noadmins(con))
print()
print('--------------------')
print()

#print(get_plants(con))
#insert_plant(con, 'qqq', 'www', 'eee')
#delete_plant(con, 6)
#update_plant_name(con, 7, 'IVAN!')
#print(get_plants(con))

print(get_soils_grounds_plants_animals_for_territories(con, 43.03, 131.88))


print()