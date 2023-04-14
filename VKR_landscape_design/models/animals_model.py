import pandas

def get_animals(conn):
    return pandas.read_sql('''
    SELECT * 
    FROM animals
    ''', conn)

def delete_animal(conn, animal_user_id):
    return pandas.read_sql('''
    DELETE FROM animals
    WHERE animal_id = :animaliddelete
    ''', conn, params={"animaliddelete": animal_user_id})