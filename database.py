import sqlite3

# ---------------- DATABASE SETUP ----------------
def create_database():

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        password TEXT,
        points INTEGER DEFAULT 0,
        level TEXT DEFAULT 'Beginner'
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


# ---------------- ADMIN ----------------
def create_admin():

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
        INSERT OR IGNORE INTO users (username, email, password)
        VALUES (?, ?, ?)
    """, ("admin", "admin@gmail.com", "1234"))

    conn.commit()
    conn.close()


# ---------------- LOGIN ----------------
def login_user(username, password):

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    data = c.fetchone()
    conn.close()
    return data


# ---------------- REGISTER ----------------
def register_user(username, email, password):

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    try:
        c.execute(
            "INSERT INTO users(username,email,password) VALUES(?,?,?)",
            (username, email, password)
        )
        conn.commit()
        return True

    except:
        return False

    finally:
        conn.close()


# ---------------- GET USER ----------------
def get_user(username):

    if not username:
        return None

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    data = c.fetchone()
    conn.close()
    return data


# ---------------- UPDATE POINTS ----------------
def update_points(username, points):

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
        UPDATE users
        SET points = points + ?
        WHERE username = ?
    """, (points, username))

    conn.commit()
    conn.close()


# ---------------- GET ALL USERS ----------------
def get_all_users():

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("SELECT * FROM users")
    data = c.fetchall()

    conn.close()
    return data
   
