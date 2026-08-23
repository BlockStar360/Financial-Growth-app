import sqlite3
DATABASE = "users.db"


def createDatabase():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            parentUsername TEXT,
            parentPassword TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            childUsername TEXT NOT NULL,
            choreName TEXT NOT NULL,
            xpAmount INTEGER NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def addChore(childUsername, choreName, xpAmount):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO chores (childUsername, choreName, xpAmount) VALUES (?, ?, ?)",
        (childUsername, choreName, xpAmount)
    )

    connection.commit()
    connection.close()


def getChoresFor(childUsername):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT choreName, xpAmount FROM chores WHERE childUsername = ?",
        (childUsername,)
    )

    rows = cursor.fetchall()
    connection.close()

    #A list of tuples with chore name and xp amount
    return rows


def checkUser(username, password):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )

    user = cursor.fetchone()
    connection.close()

    return user is not None


def addUser(username, password):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password)
    )

    connection.commit()
    connection.close()


def parentExistsFor(childUsername):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT parentUsername FROM users WHERE username = ?",
        (childUsername,)
    )

    row = cursor.fetchone()
    connection.close()

    #Row 0 is for parentUsername
    return row is not None and row[0] is not None


def setParentCredentials(childUsername, parentUsername, parentPassword):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE users SET parentUsername = ?, parentPassword = ? WHERE username = ?",
        (parentUsername, parentPassword, childUsername)
    )

    connection.commit()
    connection.close()


def checkParent(childUsername, parentUsername, parentPassword):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND parentUsername = ? AND parentPassword = ?",
        (childUsername, parentUsername, parentPassword)
    )

    row = cursor.fetchone()
    connection.close()

    return row is not None