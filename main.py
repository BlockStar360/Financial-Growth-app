import tkinter as tk
from login import loginPage
from database import createDatabase

createDatabase() #Makes the database for usernames, password and other data

root = tk.Tk()

loginPage(root) #Run the login screen

root.mainloop() #Keeps the window open