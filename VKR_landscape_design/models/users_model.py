import pandas

def get_users(conn):
    return pandas.read_sql('''
    SELECT * 
    FROM users
    ''', conn)

def get_users_without_password(conn):
    return pandas.read_sql('''
    SELECT user_login, user_email, user_surname, user_name, user_fathername, user_isFemale, user_picture, user_isAdmin
    FROM users
    ''', conn)

def get_users_without_password_admins(conn):
    return pandas.read_sql('''
    SELECT user_login, user_email, user_surname, user_name, user_fathername, user_isFemale, user_picture
    FROM users
    WHERE user_isAdmin = TRUE
    ''', conn)

def get_users_without_password_noadmins(conn):
    return pandas.read_sql('''
    SELECT user_login, user_email, user_surname, user_name, user_fathername, user_isFemale, user_picture
    FROM users
    WHERE user_isAdmin = FALSE
    ''', conn)

def insert_user(conn, user_user_login, user_user_password, user_user_email, user_user_isAdmin):
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO users(user_login, user_password, user_email, user_isAdmin) VALUES (:userlogin, :userpassword, :useremail, :userisadmin)
        ''', {"userlogin": user_user_login, "userpassword": user_user_password, "useremail": user_user_email, "userisadmin": user_user_isAdmin})
    conn.commit()

def delete_user(conn, user_user_id):
    cur = conn.cursor()
    cur.execute('''
        DELETE FROM users WHERE user_id = :useriddelete
        ''', {"useriddelete": user_user_id})
    conn.commit()


def update_user_login(conn, user_user_id, user_user_login):
    cur = conn.cursor()
    cur.execute('''
        UPDATE users 
        SET user_login = :userlogin 
        WHERE user_id = :useridupdate
        ''', {"useridupdate": user_user_id, "userlogin": user_user_login})
    conn.commit()

