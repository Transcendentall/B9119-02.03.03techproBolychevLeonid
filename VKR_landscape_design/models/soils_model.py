import pandas

def get_soils(conn):
    return pandas.read_sql('''
    SELECT * 
    FROM soils
    ''', conn)

def get_one_soil(conn, user_soil_id):
    return pandas.read_sql('''
    SELECT * 
    FROM soils
    WHERE soil_id = ''' + str(user_soil_id), conn)

def get_grounds_for_soil(conn, user_soil_id):
    return pandas.read_sql('''
    SELECT DISTINCT * 
    FROM soils 
    JOIN connection_soils_grounds ON (soils.soil_id = connection_soils_grounds.connection_soil_id) 
    JOIN grounds ON (connection_soils_grounds.connection_ground_id = grounds.ground_id) 
    WHERE soil_id = ''' + str(user_soil_id), conn)

def get_plants_for_soil(conn, user_soil_id):
    return pandas.read_sql('''
    SELECT DISTINCT * 
    FROM soils 
    JOIN connection_soils_plants ON (soils.soil_id = connection_soils_plants.connection_soil_id) 
    JOIN plants ON (connection_soils_plants.connection_plant_id = plants.plant_id) 
    WHERE soil_id = ''' + str(user_soil_id), conn)

def insert_soil(conn, user_soil_name, user_soil_description):
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO soils(soil_name, soil_description) 
        VALUES (:usersoilname, :usersoildescription)
        ''', {"usersoilname": user_soil_name, "usersoildescription": user_soil_description})
    conn.commit()

def delete_soil(conn, user_soil_id):
    cur = conn.cursor()
    cur.execute('''
        DELETE FROM soils WHERE soil_id = :soiliddelete
        ''', {"soiliddelete": user_soil_id})
    conn.commit()

def update_soil_name(conn, user_soil_id, user_soil_name):
    cur = conn.cursor()
    cur.execute('''
        UPDATE soils 
        SET soil_name = :usersoilname 
        WHERE soil_id = :usersoilid
        ''', {"usersoilid": user_soil_id, "usersoilname": user_soil_name})
    conn.commit()

def update_soil_description(conn, user_soil_id, user_soil_description):
    cur = conn.cursor()
    cur.execute('''
        UPDATE soils 
        SET soil_description = :usersoildescription 
        WHERE soil_id = :usersoilid
        ''', {"usersoilid": user_soil_id, "usersoildescription": user_soil_description})
    conn.commit()

def update_soil_acidity(conn, user_soil_id, user_soil_acidity):
    cur = conn.cursor()
    cur.execute('''
        UPDATE soils 
        SET soil_acidity = :usersoilacidity 
        WHERE soil_id = :usersoilid
        ''', {"usersoilid": user_soil_id, "usersoilacidity": user_soil_acidity})
    conn.commit()

def update_soil_minerals(conn, user_soil_id, user_soil_minerals):
    cur = conn.cursor()
    cur.execute('''
        UPDATE soils 
        SET soil_minerals = :usersoilminerals 
        WHERE soil_id = :usersoilid
        ''', {"usersoilid": user_soil_id, "usersoilminerals": user_soil_minerals})
    conn.commit()

def update_soil_profile(conn, user_soil_id, user_soil_profile):
    cur = conn.cursor()
    cur.execute('''
        UPDATE soils 
        SET soil_profile = :usersoilprofile 
        WHERE soil_id = :usersoilid
        ''', {"usersoilid": user_soil_id, "usersoilprofile": user_soil_profile})
    conn.commit()

def update_soil_picture(conn, user_soil_id, user_soil_picture):
    cur = conn.cursor()
    cur.execute('''
        UPDATE soils 
        SET soil_picture = :usersoilpicture 
        WHERE soil_id = :usersoilid
        ''', {"usersoilid": user_soil_id, "usersoilpicture": user_soil_picture})
    conn.commit()

