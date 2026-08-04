import tkinter as tk
from tkinter import messagebox

def add_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(fg="light grey")

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="grey")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

def userLogin(entry):
    username = entry
    if not username:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return
    messagebox.showinfo("You Entered", f"Hello, {username}!")

#Create the log in window
def loginPage():
    root = tk.Tk()
    root.title("Login")
    root.geometry("300x550")  #Width x Height
    root.resizable(False, False)  #Disable resizing

    #Create the label text
    label = tk.Label(root, text="Welcome to APP NAME", font=("Noto Sans HK Black", 12))
    label.pack(pady=10)

    #Create text fields for username and password
    entry = tk.Entry(root, width=25, font=("Noto Sans HK Black", 12))
    entry.pack(pady=5)
    add_placeholder(entry, "Username")

    entry = tk.Entry(root, width=25, font=("Noto Sans HK Black", 12))
    entry.pack(pady=5)
    add_placeholder(entry, "Password")

    #Create the submit button
    submit_btn = tk.Button(root, 
                           text="Log In", 
                           command=lambda:userLogin(entry.get().strip()), 
                           font=("Noto Sans HK Black", 12)
                           )
    submit_btn.pack(pady=10)

    #Start the Tkinter event loop
    root.mainloop()


loginPage()