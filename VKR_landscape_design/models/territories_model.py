import pandas

def get_territories(conn):
    return pandas.read_sql('''
    SELECT * 
    FROM territories
    ''', conn)

def get_one_territorie(conn, user_territorie_id):
    return pandas.read_sql('''
    SELECT * 
    FROM territories
    WHERE territorie_id = ''' + str(user_territorie_id), conn)

def bycoord(conn, user_territorie_coord_x, user_territorie_coord_y):
    err = 0.05
    return pandas.read_sql('''
    SELECT DISTINCT soil_id, soil_name, soil_description, soil_picture, ground_name, ground_description, ground_picture, plant_id, plant_name, plant_description, plant_climat, plant_temperature_min, plant_temperature_max, connection_soils_plants_isGood, plant_picture, animal_id, animal_name, animal_description, animal_picture
    FROM territories 
    JOIN connection_territories_soils ON (territories.territorie_id = connection_territories_soils.connection_territorie_id) 
    JOIN soils ON (connection_territories_soils.connection_soil_id = soils.soil_id) 
    JOIN connection_soils_grounds ON (soils.soil_id = connection_soils_grounds.connection_soil_id) 
    JOIN grounds ON (connection_soils_grounds.connection_ground_id = grounds.ground_id) 
    JOIN connection_soils_plants ON (soils.soil_id = connection_soils_plants.connection_soil_id) 
    JOIN plants ON (connection_soils_plants.connection_plant_id = plants.plant_id) 
    JOIN connection_plants_animals ON (plants.plant_id = connection_plants_animals.connection_plant_id) 
    JOIN animals ON (connection_plants_animals.connection_animal_id = animals.animal_id)
    WHERE territorie_coord_x <= ''' + str(user_territorie_coord_x + err) +
    ' AND territorie_coord_x >=  ' + str(user_territorie_coord_x - err) +
    ' AND territorie_coord_y <=  ' + str(user_territorie_coord_y + err) +
    ' AND territorie_coord_y >=  ' + str(user_territorie_coord_y - err)
                           , conn)

def insert_territorie(conn, user_territorie_coord_x, user_territorie_coord_y, user_territorie_coord_z):
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO territories(territorie_coord_x, territorie_coord_y, territorie_coord_z) 
        VALUES (:userterritoriecoordx, :userterritoriecoordy, :userterritoriecoordz)
        ''', {"userterritoriecoordx": user_territorie_coord_x, "userterritoriecoordy": user_territorie_coord_y, "userterritoriecoordz": user_territorie_coord_z})
    conn.commit()

def delete_territorie(conn, user_territorie_id):
    cur = conn.cursor()
    cur.execute('''
        DELETE FROM territories WHERE territorie_id = :territorieiddelete
        ''', {"territorieiddelete": user_territorie_id})
    conn.commit()

def update_territorie_coord_x(conn, user_territorie_id, user_territorie_coord_x):
    cur = conn.cursor()
    cur.execute('''
        UPDATE territories 
        SET territorie_coord_x = :userterritoriecoordx 
        WHERE territorie_id = :userterritorieid
        ''', {"userterritorieid": user_territorie_id, "userterritoriecoordx": user_territorie_coord_x})
    conn.commit()

def update_territorie_coord_y(conn, user_territorie_id, user_territorie_coord_y):
    cur = conn.cursor()
    cur.execute('''
        UPDATE territories 
        SET territorie_coord_y = :userterritoriecoordy 
        WHERE territorie_id = :userterritorieid
        ''', {"userterritorieid": user_territorie_id, "userterritoriecoordy": user_territorie_coord_y})
    conn.commit()

def update_territorie_coord_z(conn, user_territorie_id, user_territorie_coord_z):
    cur = conn.cursor()
    cur.execute('''
        UPDATE territories 
        SET territorie_coord_z = :userterritoriecoordz 
        WHERE territorie_id = :userterritorieid
        ''', {"userterritorieid": user_territorie_id, "userterritoriecoordz": user_territorie_coord_z})
    conn.commit()