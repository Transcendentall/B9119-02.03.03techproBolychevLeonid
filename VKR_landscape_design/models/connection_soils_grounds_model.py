import pandas

def get_connection_soils_grounds(conn):
    return pandas.read_sql('''
    SELECT * 
    FROM connection_soils_grounds
    ''', conn)

def get_one_connection_soils_grounds(conn, user_connection_soils_grounds_id):
    return pandas.read_sql('''
    SELECT * 
    FROM connection_soils_grounds
    WHERE connection_soils_grounds_id = ''' + str(user_connection_soils_grounds_id), conn)




def find_connection_soils_grounds(conn, user_connection_soil_id, user_connection_ground_id):
    return pandas.read_sql('''
    SELECT * 
    FROM connection_soils_grounds
    WHERE connection_soil_id = ''' + str(user_connection_soil_id)
                           + ' AND connection_ground_id = ' + str(user_connection_ground_id), conn)

def find_connection_soils_grounds_soil_id(conn, user_connection_soils_grounds_id, user_connection_soil_id):
    return pandas.read_sql('''
    SELECT *
    FROM connection_soils_grounds
    WHERE connection_soil_id = ''' + str(user_connection_soil_id) + ' '
    '''AND connection_ground_id IN 
    (SELECT connection_ground_id 
    FROM connection_soils_grounds
    WHERE connection_soils_grounds_id = ''' + str(user_connection_soils_grounds_id) + ')', conn)

def find_connection_soils_grounds_ground_id(conn, user_connection_soils_grounds_id, user_connection_ground_id):
    return pandas.read_sql('''
    SELECT *
    FROM connection_soils_grounds
    WHERE connection_ground_id = ''' + str(user_connection_ground_id) + ' '
    '''AND connection_soil_id IN 
    (SELECT connection_soil_id 
    FROM connection_soils_grounds
    WHERE connection_soils_grounds_id = ''' + str(user_connection_soils_grounds_id) + ')', conn)





def insert_connection_soils_grounds(conn, user_connection_soil_id, user_connection_ground_id):
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO connection_soils_grounds(connection_soil_id, connection_ground_id) 
        VALUES (:userconnectionsoilid, :userconnectiongroundid)
        ''', {"userconnectionsoilid": user_connection_soil_id, "userconnectiongroundid": user_connection_ground_id})
    conn.commit()

def delete_connection_soils_grounds(conn, user_connection_soils_grounds_id):
    cur = conn.cursor()
    cur.execute('''
        DELETE FROM connection_soils_grounds WHERE connection_soils_grounds_id = :connectionsoilsgroundsiddelete
        ''', {"connectionsoilsgroundsiddelete": user_connection_soils_grounds_id})
    conn.commit()

def update_connection_soils_grounds_soil_id(conn, user_connection_soils_grounds_id, user_connection_soil_id):
    cur = conn.cursor()
    cur.execute('''
        UPDATE connection_soils_grounds 
        SET connection_soil_id = :userconnectionsoilid 
        WHERE connection_soils_grounds_id = :userconnectionsoilsgroundsid
        ''', {"userconnectionsoilsgroundsid": user_connection_soils_grounds_id, "userconnectionsoilid": user_connection_soil_id})
    conn.commit()

def update_connection_soils_grounds_ground_id(conn, user_connection_soils_grounds_id, user_connection_ground_id):
    cur = conn.cursor()
    cur.execute('''
        UPDATE connection_soils_grounds 
        SET connection_ground_id = :userconnectiongroundid
        WHERE connection_soils_grounds_id = :userconnectionsoilsgroundsid
        ''', {"userconnectionsoilsgroundsid": user_connection_soils_grounds_id, "userconnectiongroundid": user_connection_ground_id})
    conn.commit()