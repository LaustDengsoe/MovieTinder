from MovieTinder import conn, login_manager
from flask_login import UserMixin
from psycopg2 import sql


class User(tuple, UserMixin):
    def __init__(self, user_data):
        self.username = user_data[0]
        self.password = user_data[1]
        self.id = user_data[2]
        self.role = "user"

    def get_id(self):
       return (self.id)
    
class Friendship(tuple):
    def __init__(self, friendship_data):
        self.id1 = friendship_data[0]
        self.id2 = friendship_data[1]

    
class Movie(tuple):
    def __init__(self, movie_data):
        self.id = movie_data[0]
        self.imdb_id = movie_data[1]
        self.title = movie_data[2]
        self.year = movie_data[3]
        self.summary = movie_data[4]

    def get_id(self):
       return (self.id)

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

def select_new_Movie(user_id):
    cur = conn.cursor()
    sql = """
    SELECT * FROM Movies
    WHERE id NOT IN (
        SELECT movie_id FROM Likes
        WHERE user_id = %s
    )
    ORDER BY RANDOM()
    LIMIT 1
    """
    cur.execute(sql, (user_id,))
    movie = Movie(cur.fetchone()) if cur.rowcount > 0 else None;
    cur.close()
    return movie

def insert_Like(user_id, movie_id):
    cur = conn.cursor()
    sql = """
    INSERT INTO Likes(user_id, movie_id)
    VALUES (%s, %s)
    """
    cur.execute(sql, (user_id, movie_id,))
    conn.commit()
    cur.close()

def select_Friends(user_id):
    cur = conn.cursor()
    sql = """
    SELECT username FROM Users
    WHERE id IN (
        SELECT id2 FROM HasFriends
        WHERE id1 = %s 
    )
    """
    cur.execute(sql, (user_id,))
    users = cur.fetchall() if cur.rowcount > 0 else None;
    cur.close()
    return users

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