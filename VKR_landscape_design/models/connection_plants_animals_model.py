import pandas

def get_connection_plants_animals(conn):
    return pandas.read_sql('''
    SELECT * 
    FROM connection_plants_animals
    ''', conn)

def insert_connection_plants_animals(conn, user_connection_plant_id, user_connection_animal_id):
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO connection_plants_animals(connection_plant_id, connection_animal_id) 
        VALUES (:userconnectionplantid, :userconnectionanimalid)
        ''', {"userconnectionplantid": user_connection_plant_id, "userconnectionanimalid": user_connection_animal_id})
    conn.commit()

def delete_connection_plants_animals(conn, user_connection_plants_animals_id):
    cur = conn.cursor()
    cur.execute('''
        DELETE FROM connection_plants_animals WHERE connection_plants_animals_id = :connectionplantsanimalsiddelete
        ''', {"connectionplantsanimalsiddelete": user_connection_plants_animals_id})
    conn.commit()

def update_connection_plants_animals_plant_id(conn, user_connection_plants_animals_id, user_connection_plant_id):
    cur = conn.cursor()
    cur.execute('''
        UPDATE connection_plants_animals 
        SET connection_plant_id = :userconnectionplantid 
        WHERE connection_plants_animals_id = :userconnectionplantsanimalsid
        ''', {"userconnectionplantsanimalsid": user_connection_plants_animals_id, "userconnectionplantid": user_connection_plant_id})
    conn.commit()

def update_connection_plants_animals_animal_id(conn, user_connection_plants_animals_id, user_connection_animal_id):
    cur = conn.cursor()
    cur.execute('''
        UPDATE connection_plants_animals 
        SET connection_animal_id = :userconnectionanimalid
        WHERE connection_plants_animals_id = :userconnectionplantsanimalsid
        ''', {"userconnectionplantsanimalsid": user_connection_plants_animals_id, "userconnectionanimalid": user_connection_animal_id})
    conn.commit()
