from MovieTinder import conn, login_manager
from flask_login import UserMixin
from psycopg2 import sql



@login_manager.user_loader
def load_user(password):
    cur = conn.cursor()

    user_sql = sql.SQL("""
    SELECT * FROM Users
    WHERE password = %s
    """)

    cur.execute(user_sql, (password,))

    if cur.rowcount > 0:
        return User(cur.fetchone())
    else:
        return None

class User(tuple, UserMixin):
    def __init__(self, user_data):
        self.username = user_data[0]
        self.password = user_data[1]
        self.id = user_data[2]
        self.role = "user"

    def get_id(self):
       return (self.id)
    
def select_User(username):
    cur = conn.cursor()
    sql = """
    SELECT * FROM Users
    WHERE username = %s
    """
    cur.execute(sql, (username,))
    user = User(cur.fetchone()) if cur.rowcount > 0 else None;
    cur.close()
    return user

def insert_User(username, password):
    cur = conn.cursor()
    sql = """
    INSERT INTO Users(username, password)
    VALUES (%s, %s)
    """
    cur.execute(sql, (username, password,))
    conn.commit()
    cur.close()

def update_Username(id, username):
    cur = conn.cursor()
    sql = """
    UPDATE Users
    SET username = %s
    WHERE id = %s
    """
    cur.execute(sql, (username, id,))
    conn.commit()
    cur.close()

def update_Pass(id, password):
    cur = conn.cursor()
    sql = """
    UPDATE Users
    SET password = %s
    WHERE id = %s
    """
    cur.execute(sql, (password, id,))
    conn.commit()
    cur.close()