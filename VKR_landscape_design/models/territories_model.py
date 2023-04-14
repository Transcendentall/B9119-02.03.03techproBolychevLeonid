import pandas

def get_territories(conn):
    return pandas.read_sql('''
    SELECT * 
    FROM territories
    ''', conn)

def delete_territorie(conn, territorie_user_id):
    return pandas.read_sql('''
    DELETE FROM territories
    WHERE territorie_id = :territorieiddelete
    ''', conn, params={"territorieiddelete": territorie_user_id})