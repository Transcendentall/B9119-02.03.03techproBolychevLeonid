import pandas

def get_users(conn):
    return pandas.read_sql('''
    SELECT * 
    FROM users
    ''', conn)

def delete_user(conn, user_user_id):
    return pandas.read_sql('''
    DELETE FROM users
    WHERE user_id = :useriddelete
    ''', conn, params={"useriddelete": user_user_id})