import pandas

def get_grounds(conn):
    return pandas.read_sql('''
    SELECT * 
    FROM grounds
    ''', conn)

def delete_ground(conn, ground_user_id):
    return pandas.read_sql('''
    DELETE FROM grounds
    WHERE ground_id = :groundiddelete
    ''', conn, params={"groundiddelete": ground_user_id})