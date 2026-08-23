import tkinter as tk
import session
from functions import showPopup, addPlaceholder, getRealValue
from database import checkParent, setParentCredentials, parentExistsFor


def parentLogin(parentUsername, parentPassword, childUsername, root):
    if not parentUsername or not parentPassword:
        showPopup(root, "Error", "Please fill out both fields")
        return
    if checkParent(childUsername, parentUsername, parentPassword):
        showPopup(root, "Login successful!", f"Welcome {parentUsername}!")
        from addChore import addChorePage
        addChorePage(root, childUsername)
    else:
        showPopup(root, "Error", "Incorrect username or password")

#Sign up verification
def parentSignup(parentUsername, parentPassword, childUsername, root):
    if not parentUsername or not parentPassword:
        showPopup(root, "Error", "Please fill out both fields")
        return
    if parentExistsFor(childUsername):
        showPopup(root, "Error", "Account already exists")
        return
    setParentCredentials(childUsername, parentUsername, parentPassword)
    showPopup(root, "Success", "Parent account created")


#Create the parent login window
def parentLoginPage(root):
    childUsername = session.currentUsername

    if not childUsername:
        #Just in case, shouldn't actually happen
        showPopup(root, "Error", "No user is currently logged in")
        return

    for widget in root.winfo_children():
        widget.destroy()

    root.title("Parent Login")
    root.geometry("300x550")
    root.resizable(False, False)

    #Create the label text
    label = tk.Label(root, text="Parent Login", font=("Noto Sans HK Black", 12))
    label.pack(pady=10)

    #Create text fields for parent username and password
    usernameEntry = tk.Entry(root, width=25, font=("Noto Sans HK Black", 12))
    usernameEntry.pack(pady=5)
    addPlaceholder(usernameEntry, "Username")

    passwordEntry = tk.Entry(root, width=25, font=("Noto Sans HK Black", 12))
    passwordEntry.pack(pady=5)
    addPlaceholder(passwordEntry, "Password")

    #Create the login button
    loginButton = tk.Button(root,
                           text="Log In",
                           command=lambda: parentLogin(getRealValue(usernameEntry), getRealValue(passwordEntry), childUsername, root),
                           font=("Noto Sans HK Black", 12),
                           )
    loginButton.pack(pady=10)

    #Create the sign up button
    signupButton = tk.Button(root,
                            text="Sign Up",
                            command=lambda: parentSignup(getRealValue(usernameEntry), getRealValue(passwordEntry), childUsername, root),
                            font=("Noto Sans HK Black", 12)
                            )
    signupButton.pack(pady=10)

    #Create the back button
    from choreList import choresPage
    backButton = tk.Button(root,
                          text="Back",
                          command=lambda: choresPage(root),
                          font=("Noto Sans HK Black", 12)
                          )
    backButton.pack(pady=10)