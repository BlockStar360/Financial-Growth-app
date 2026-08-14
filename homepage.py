import tkinter as tk

def homePage(root):
    root.title("Home")
    root.geometry("300x550") #Width x Height
    root.resizable(False, False) #Disable resizing

    label = tk.Label(
        root,
        text="Home Page",
        font=("Noto Sans HK Black", 12)
    )
    label.pack(pady=10)