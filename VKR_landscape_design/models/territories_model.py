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
    # ABS(territorie_coord_x - ''' + str(user_territorie_coord_x) + '''), ABS(territorie_coord_y - ''' + str(user_territorie_coord_y) + '''), SQRT(ABS(territorie_coord_x - ''' + str(user_territorie_coord_x) + ''') + ABS(territorie_coord_y - ''' + str(user_territorie_coord_y) + '''))
    return pandas.read_sql('''
    SELECT DISTINCT territorie_id 
    FROM territories 
    WHERE territorie_coord_x <= ''' + str(user_territorie_coord_x + err) +
    ' AND territorie_coord_x >=  ' + str(user_territorie_coord_x - err) +
    ' AND territorie_coord_y <=  ' + str(user_territorie_coord_y + err) +
    ' AND territorie_coord_y >=  ' + str(user_territorie_coord_y - err) +
    ' ORDER by (SQRT(ABS(territorie_coord_x - ' + str(user_territorie_coord_x) + ') + ABS(territorie_coord_y - ' + str(user_territorie_coord_y) + ')))'
    ' LIMIT 1', conn)

def byterritorie_soil(conn, user_territorie_id):
    return pandas.read_sql('''
    SELECT DISTINCT territorie_id, soil_id, soil_name, soil_description, soil_acidity, soil_minerals, soil_profile, soil_picture
    FROM territories 
    JOIN connection_territories_soils ON (territories.territorie_id = connection_territories_soils.connection_territorie_id) 
    JOIN soils ON (connection_territories_soils.connection_soil_id = soils.soil_id) 
    WHERE territorie_id = ''' + str(user_territorie_id), conn)

def byterritorie_ground(conn, user_territorie_id):
    return pandas.read_sql('''
    SELECT DISTINCT territorie_id, ground_id, ground_name, ground_description, ground_density, ground_humidity, ground_hardness_Moos, ground_picture
    FROM territories 
    JOIN connection_soils_grounds ON (soils.soil_id = connection_soils_grounds.connection_soil_id) 
    JOIN grounds ON (connection_soils_grounds.connection_ground_id = grounds.ground_id) 
    JOIN connection_territories_soils ON (territories.territorie_id = connection_territories_soils.connection_territorie_id) 
    JOIN soils ON (connection_territories_soils.connection_soil_id = soils.soil_id) 
    WHERE territorie_id = ''' + str(user_territorie_id), conn)

def byterritorie_plant(conn, user_territorie_id):
    return pandas.read_sql('''
    SELECT DISTINCT territorie_id, connection_soils_plants_isGood, plant_id, plant_name, plant_description, plant_isFodder, plant_isExactingToTheLight, plant_isOneYear, plant_isTwoYears, plant_isManyYears, plant_climat, plant_required_minerals_and_trace_elements, plant_temperature_min, plant_temperature_max, plant_kingdom, plant_philum, plant_class, plant_order, plant_family, plant_genus, plant_species, plant_picture
    FROM territories 
    JOIN connection_territories_soils ON (territories.territorie_id = connection_territories_soils.connection_territorie_id) 
    JOIN soils ON (connection_territories_soils.connection_soil_id = soils.soil_id) 
    JOIN connection_soils_grounds ON (soils.soil_id = connection_soils_grounds.connection_soil_id) 
    JOIN grounds ON (connection_soils_grounds.connection_ground_id = grounds.ground_id) 
    JOIN connection_soils_plants ON (soils.soil_id = connection_soils_plants.connection_soil_id) 
    JOIN plants ON (connection_soils_plants.connection_plant_id = plants.plant_id) 
    WHERE territorie_id = ''' + str(user_territorie_id), conn)

def byterritorie_animal(conn, user_territorie_id):
    return pandas.read_sql('''
    SELECT DISTINCT territorie_id, animal_id, animal_name, animal_description, animal_kingdom, animal_philum, animal_class, animal_order, animal_family, animal_genus, animal_species, animal_picture 
    FROM territories 
    JOIN connection_territories_soils ON (territories.territorie_id = connection_territories_soils.connection_territorie_id) 
    JOIN soils ON (connection_territories_soils.connection_soil_id = soils.soil_id) 
    JOIN connection_soils_grounds ON (soils.soil_id = connection_soils_grounds.connection_soil_id) 
    JOIN grounds ON (connection_soils_grounds.connection_ground_id = grounds.ground_id) 
    JOIN connection_soils_plants ON (soils.soil_id = connection_soils_plants.connection_soil_id) 
    JOIN plants ON (connection_soils_plants.connection_plant_id = plants.plant_id) 
    JOIN connection_plants_animals ON (plants.plant_id = connection_plants_animals.connection_plant_id) 
    JOIN animals ON (connection_plants_animals.connection_animal_id = animals.animal_id)
    WHERE territorie_id = ''' + str(user_territorie_id), conn)


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

