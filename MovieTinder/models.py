from MovieTinder import conn, login_manager
from flask_login import UserMixin
from psycopg2 import sql


class User(tuple, UserMixin):
    def __init__(self, user_data):
        self.id = user_data[0]
        self.username = user_data[1]
        self.password = user_data[2] if len(user_data) > 2 else None

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
def load_user(id):
    cur = conn.cursor()

    user_sql = sql.SQL("""
    SELECT * FROM Users
    WHERE id = %s
    """)

    cur.execute(user_sql, (id,))

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
    AND id NOT IN (
        SELECT movie_id FROM Dislikes
        WHERE user_id = %s
    )
    ORDER BY RANDOM()
    LIMIT 1
    """
    cur.execute(sql, (user_id,user_id,))
    movie = Movie(cur.fetchone()) if cur.rowcount > 0 else None;
    cur.close()
    return movie

def select_all_liked_movies(user_id):
    cur = conn.cursor()
    sql = """
    SELECT * FROM Movies
    WHERE id IN (
        SELECT movie_id FROM Likes
        WHERE user_id = %s
    )
    """
    cur.execute(sql, (user_id,))
    movies = [Movie(row) for row in cur.fetchall()] if cur.rowcount > 0 else None;
    cur.close()
    return movies

def insert_Like(user_id, movie_id):
    cur = conn.cursor()
    sql = """
    INSERT INTO Likes(user_id, movie_id)
    VALUES (%s, %s)
    """
    cur.execute(sql, (user_id, movie_id,))
    conn.commit()
    cur.close()

def insert_Dislike (user_id, movie_id):
    cur = conn.cursor()
    sql = """
    INSERT INTO Dislikes(user_id, movie_id)
    VALUES (%s, %s)
    """
    cur.execute(sql, (user_id, movie_id,))
    conn.commit()
    cur.close()

def select_Friends(user_id):
    cur = conn.cursor()
    sql = """
    SELECT id, username FROM Users
    WHERE id IN (
        SELECT id2 FROM HasFriends
        WHERE id1 = %s 
    ) OR id IN (
        SELECT id1 FROM HasFriends
        WHERE id2 = %s
    )
    """
    cur.execute(sql, (user_id, user_id,))
    users = [User(row) for row in cur.fetchall()] if cur.rowcount > 0 else None;
    cur.close()
    return users

def select_Users_Search(user_id, regex):
    cur = conn.cursor()
    sql = """
    SELECT id, username FROM Users
    WHERE username ~ %s AND id != %s
    """
    cur.execute(sql, (regex, user_id,))
    users = [User(row) for row in cur.fetchall()] if cur.rowcount > 0 else None;
    cur.close()
    return users

def delete_Friend(user_id, friend_id):
    cur = conn.cursor()
    sql = """
    DELETE FROM HasFriends
    WHERE (id1 = %s AND id2 = %s)
    OR (id1 = %s AND id2 = %s)
    """
    cur.execute(sql, (user_id, friend_id, friend_id, user_id,))
    conn.commit()
    cur.close()

def insert_Friend(user_id, add_id):
    cur = conn.cursor()
    sql = """
    INSERT INTO HasFriends(id1, id2)
    VALUES (%s, %s)
    """
    cur.execute(sql, (user_id, add_id,))
    conn.commit()
    cur.close()

def select_Friend(id):
    cur = conn.cursor()
    sql = """
    SELECT id, username FROM Users
    WHERE id = %s
    """
    cur.execute(sql, (id,))
    friend = User(cur.fetchone()) if cur.rowcount > 0 else None;
    cur.close()
    return friend

def select_common_Movies(user_id, friend_id):
    cur = conn.cursor()
    sql = """
    SELECT * FROM Movies
    WHERE id IN (
        SELECT movie_id FROM Likes
        WHERE user_id = %s
    )
    AND id IN (
        SELECT movie_id FROM Likes
        WHERE user_id = %s
    )
    """
    cur.execute(sql, (user_id, friend_id,))
    movies = [Movie(row) for row in cur.fetchall()] if cur.rowcount > 0 else None;
    cur.close()
    return movies