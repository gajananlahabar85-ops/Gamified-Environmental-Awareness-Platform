import sqlite3


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

    data=c.fetchone()

    conn.close()

    return data
