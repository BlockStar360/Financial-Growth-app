import sqlite3
DATABASE = "users.db"


#Creates the database used to store information for individual accounts
def createDatabase():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            parentUsername TEXT,
            parentPassword TEXT,
            xp INTEGER NOT NULL DEFAULT 0
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


#Adds a chore that will appear as a box on the chores list
def addChore(childUsername, choreName, xpAmount):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO chores (childUsername, choreName, xpAmount) VALUES (?, ?, ?)",
        (childUsername, choreName, xpAmount)
    )

    connection.commit()
    connection.close()


#Returns all the chores currently assigned to the account
def getChoresFor(childUsername):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, choreName, xpAmount FROM chores WHERE childUsername = ?",
        (childUsername,)
    )

    rows = cursor.fetchall()
    connection.close()

    #A list of tuples with chore name and xp amount
    return rows


#Removes a chore (after the chore box is clicked)
def deleteChore(choreId):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM chores WHERE id = ?", (choreId,))

    connection.commit()
    connection.close()


#Returns the amound of xp the user currently has
def getXP(username):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("SELECT xp FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    connection.close()

    return row[0] if row else 0


def addXP(username, amount):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE users SET xp = xp + ? WHERE username = ?",
        (amount, username)
    )

    connection.commit()
    connection.close()


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