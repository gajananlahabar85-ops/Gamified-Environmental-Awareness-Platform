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

    return data
