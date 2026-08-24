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
            xp INTEGER NOT NULL DEFAULT 0,
            treeLevel INTEGER NOT NULL DEFAULT 1,
            money INTEGER NOT NULL DEFAULT 0,
            defaultOwned INTEGER NOT NULL DEFAULT 1,
            fireOwned INTEGER NOT NULL DEFAULT 0,
            glitchOwned INTEGER NOT NULL DEFAULT 0,
            galaxyOwned INTEGER NOT NULL DEFAULT 0,
            selectedSkin TEXT NOT NULL DEFAULT 'default'
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


#Adds a certain amount of money to the users account
def addMoney(username, amount):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE users SET money = money + ? WHERE username = ?",
        (amount, username)
    )

    connection.commit()
    connection.close()


#Set the tree level back to 1 so the user has to grow another one
def resetTree(username):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE users SET xp = 0, treeLevel = 1 WHERE username = ?",
        (username,)
    )

    connection.commit()
    connection.close()


#Returns the amount of money the user has
def getMoney(username):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("SELECT money FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    connection.close()

    return row[0] if row else 0


#Tries to spend the amount of money, returns True if it worked and False if the user is broke
def spendMoney(username, amount):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("SELECT money FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    currentMoney = row[0] if row else 0

    if currentMoney < amount:
        connection.close()
        return False

    cursor.execute(
        "UPDATE users SET money = money - ? WHERE username = ?",
        (amount, username)
    )

    connection.commit()
    connection.close()
    return True


#Returns which tree skins the user owns
def getSkinOwnership(username):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT defaultOwned, fireOwned, glitchOwned, galaxyOwned, selectedSkin FROM users WHERE username = ?",
        (username,)
    )
    row = cursor.fetchone()
    connection.close()

    #Just in case, shouldn't actually happen
    if row is None:
        return {"default": True, "fire": False, "glitch": False, "galaxy": False}, "default"

    defaultOwned, fireOwned, glitchOwned, galaxyOwned, selectedSkin = row
    ownership = {
        "default": bool(defaultOwned),
        "fire": bool(fireOwned),
        "glitch": bool(glitchOwned),
        "galaxy": bool(galaxyOwned)
    }
    return ownership, selectedSkin


#Changed a variable for skin owned to 1
def buySkin(username, skinName):
    column = f"{skinName}Owned"

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        f"UPDATE users SET {column} = 1 WHERE username = ?",
        (username,)
    )

    connection.commit()
    connection.close()


#Sets the currently selected skin (the last button clicked)
def selectSkin(username, skinName):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE users SET selectedSkin = ? WHERE username = ?",
        (skinName, username)
    )

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


#Returns the user's tree level (tree growth stage)
def getTreeLevel(username):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("SELECT treeLevel FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    connection.close()

    return row[0] if row else 1


def addXP(username, amount):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    #Get the current XP amount and tree level to see if it's over 100
    cursor.execute("SELECT xp, treeLevel FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    currentXP, currentLevel = row

    newXP = currentXP + amount
    newLevel = currentLevel

    #Make the tree level up when xp is over 100
    while newXP >= 100 and newLevel < 3:
        newXP -= 100
        newLevel += 1

    #Stops XP gain after the final tree level is reached
    if newLevel == 3 and newXP > 100:
        newXP = 100

    cursor.execute(
        "UPDATE users SET xp = ?, treeLevel = ? WHERE username = ?",
        (newXP, newLevel, username)
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