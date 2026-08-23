import tkinter as tk
import session
from tkinter import messagebox
from functions import addPlaceholder
from functions import showPopup, addPlaceholder, getRealValue
from database import checkUser, addUser
from homepage import homePage


def userLogin(username, password, root):
    if not username or not password:
        showPopup(root, "Error", "Please fill out both fields")
        return
    if checkUser(username, password):
        session.currentUsername = username
        showPopup(root, "Login successful!", f"Welcome {username}!")
        for widget in root.winfo_children():
            widget.destroy()
        homePage(root)
    else:
        showPopup(root, "Error", "User not found")

#Sign up verification
def userSignup(username, password, root):
    if not username or not password:
        showPopup(root, "Error", "Please fill out both fields")
        return
    addUser(username, password)
    showPopup(root, "Success", "New user ccount created")

#Create the log in window
def loginPage(root):
    root.title("Login")
    root.geometry("300x550")  #Width x Height
    root.resizable(False, False)  #Disable resizing

    #Create the label text
    label = tk.Label(root, text="Welcome to Financial Growth", font=("Noto Sans HK Black", 12))
    label.pack(pady=10)

    #Create text fields for username and password
    usernameEntry = tk.Entry(root, width=25, font=("Noto Sans HK Black", 12))
    usernameEntry.pack(pady=5)
    addPlaceholder(usernameEntry, "Username")

    passwordEntry = tk.Entry(root, width=25, font=("Noto Sans HK Black", 12))
    passwordEntry.pack(pady=5)
    addPlaceholder(passwordEntry, "Password")

    #Create the login button
    loginButton = tk.Button(root,
                           text="Log In",
                           command=lambda: userLogin(getRealValue(usernameEntry), getRealValue(passwordEntry), root),
                           font=("Noto Sans HK Black", 12),
                           )
    loginButton.pack(pady=10)

    #Create the sign up button
    signupButton = tk.Button(root,
                            text="Sign Up",
                            command=lambda: userSignup(getRealValue(usernameEntry), getRealValue(passwordEntry), root),
                            font=("Noto Sans HK Black", 12)
                            )
    signupButton.pack(pady=10)