import pandas

def get_soils(conn):
    return pandas.read_sql('''
    SELECT * 
    FROM soils
    ''', conn)

def delete_soil(conn, soil_user_id):
    return pandas.read_sql('''
    DELETE FROM soils
    WHERE soil_id = :soiliddelete
    ''', conn, params={"soiliddelete": soil_user_id})