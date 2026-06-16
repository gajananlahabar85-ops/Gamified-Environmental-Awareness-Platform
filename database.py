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

    c.execute("""
    CREATE TABLE IF NOT EXISTS challenges(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        points INTEGER
    )
    """)

    conn.commit()
    conn.close()



def create_admin():

   def create_admin():

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute(
        """
        INSERT OR IGNORE INTO users
        (username,email,password)
        VALUES(?,?,?)
        """,
        (
            "admin",
            "admin@gmail.com",
            "1234"
        )
    )

    conn.commit()
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



def get_user(username):
    # example dummy database logic
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    data = cursor.fetchone()

    conn.close()
    return data

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

    conn.commit()
    conn.close()
