import pandas

def get_territories(conn):
    return pandas.read_sql('''
    SELECT * 
    FROM territories
    ''', conn)

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