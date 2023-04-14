import pandas

def get_plants(conn):
    return pandas.read_sql('''
    SELECT * 
    FROM plants
    ''', conn)

def delete_plant(conn, plant_user_id):
    return pandas.read_sql('''
    DELETE FROM plants
    WHERE plant_id = :plantiddelete
    ''', conn, params={"plantiddelete": plant_user_id})