import sqlite3


def create_database():

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY,
        email TEXT,
        password TEXT,
        points INTEGER DEFAULT 0,
        level TEXT DEFAULT 'Beginner',
        badge TEXT DEFAULT 'None'
    )
    """)

    conn.commit()
    conn.close()



def create_admin():

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute(
        """
        INSERT OR IGNORE INTO users
        (username,email,password,points,level,badge)
        VALUES(?,?,?,?,?,?)
        """,
        (
            "admin",
            "admin@gmail.com",
            "1234",
            0,
            "Beginner",
            "None"
        )
    )

    conn.commit()
    conn.close()



def register_user(username,email,password):

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    try:
        c.execute(
            "INSERT INTO users(username,email,password) VALUES(?,?,?)",
            (username,email,password)
        )

        conn.commit()
        return True

    except:
        return False

    finally:
        conn.close()



def login_user(username,password):

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username,password)
    )

    data = c.fetchone()

    conn.close()

    return data



def get_user(username):

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    data = c.fetchone()

    conn.close()



    def update_points(username, points):

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute(
        """
        UPDATE users
        SET points = points + ?
        WHERE username = ?
        """,
        (points, username)
    )

    # Level update
    c.execute(
        """
        UPDATE users
        SET level =
        CASE
            WHEN points >= 200 THEN 'Earth Protector'
            WHEN points >= 100 THEN 'Green Champion'
            WHEN points >= 50 THEN 'Eco Warrior'
            ELSE 'Beginner'
        END
        WHERE username = ?
        """,
        (username,)
    )

    conn.commit()
    conn.close()
    
    return data
