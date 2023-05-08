import pandas


def get_connection_soils_plants(conn):
    return pandas.read_sql('''
    SELECT * 
    FROM connection_soils_plants
    ''', conn)

def insert_connection_soils_plants(conn, user_connection_soil_id, user_connection_plant_id, user_connection_soils_plants_isGood):
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO connection_soils_plants(connection_soil_id, connection_plant_id, connection_soils_plants_isGood) 
        VALUES (:userconnectionsoilid, :userconnectionplantid, :userconnectionsoilsplantsisGood)
        ''', {"userconnectionsoilid": user_connection_soil_id, "userconnectionplantid": user_connection_plant_id, "userconnectionsoilsplantsisGood": user_connection_soils_plants_isGood})
    conn.commit()

def delete_connection_soils_plants(conn, user_connection_soils_plants_id):
    cur = conn.cursor()
    cur.execute('''
        DELETE FROM connection_soils_plants WHERE connection_soils_plants_id = :connectionsoilsplantsiddelete
        ''', {"connectionsoilsplantsiddelete": user_connection_soils_plants_id})
    conn.commit()

def update_connection_soils_plants_soil_id(conn, user_connection_soils_plants_id, user_connection_soil_id):
    cur = conn.cursor()
    cur.execute('''
        UPDATE connection_soils_plants 
        SET connection_soil_id = :userconnectionsoilid 
        WHERE connection_soils_plants_id = :userconnectionsoilsplantsid
        ''', {"userconnectionsoilsplantsid": user_connection_soils_plants_id, "userconnectionsoilid": user_connection_soil_id})
    conn.commit()

def update_connection_soils_plants_plant_id(conn, user_connection_soils_plants_id, user_connection_plant_id):
    cur = conn.cursor()
    cur.execute('''
        UPDATE connection_soils_plants 
        SET connection_plant_id = :userconnectionplantid
        WHERE connection_soils_plants_id = :userconnectionsoilsplantsid
        ''', {"userconnectionsoilsplantsid": user_connection_soils_plants_id, "userconnectionplantid": user_connection_plant_id})
    conn.commit()

def update_connection_soils_plants_isGood(conn, user_connection_soils_plants_id, user_connection_soils_plants_isGood):
    cur = conn.cursor()
    cur.execute('''
        UPDATE connection_soils_plants 
        SET connection_soils_plants_isGood = :userconnectionsoilsplantsisGood
        WHERE connection_soils_plants_id = :userconnectionsoilsplantsid
        ''', {"userconnectionsoilsplantsid": user_connection_soils_plants_id, "userconnectionsoilsplantsisGood": user_connection_soils_plants_isGood})
    conn.commit()