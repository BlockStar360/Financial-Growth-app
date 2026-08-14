import tkinter as tk
from tkinter import messagebox
from functions import addPlaceholder
from database import checkUser, addUser
from homepage import homePage


def userLogin(usernameEntry, passwordEntry, root):
    username = usernameEntry
    password = passwordEntry
    if not username or not password:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return
    if checkUser(username, password):
        messagebox.showinfo(
            "Login Worked",
            f"Welcome {username}!"
        )
        for widget in root.winfo_children():
            widget.destroy()
        homePage(root)
    else:
        messagebox.showerror(
            "Login Failed",
            "Incorrect username or password."
        )

#Create the log in window
def loginPage(root):
    root.title("Login")
    root.geometry("300x550")  #Width x Height
    root.resizable(False, False)  #Disable resizing

    #Create the label text
    label = tk.Label(root, text="Welcome to APP NAME", font=("Noto Sans HK Black", 12))
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
                           command=lambda:userLogin(usernameEntry.get().strip(), passwordEntry.get().strip(),
                                                    root),
                           font=("Noto Sans HK Black", 12),
                           )
    loginButton.pack(pady=10)

    #Create the sign up button
    loginButton = tk.Button(root, 
                            text="Sign Up", 
                            command=lambda:addUser(usernameEntry.get().strip(), passwordEntry.get().strip()), 
                            font=("Noto Sans HK Black", 12)
                            )
    loginButton.pack(pady=10)