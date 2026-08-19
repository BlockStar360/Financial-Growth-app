import tkinter as tk


def choresPage(root):

    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(
        root,
        text="Chores Page",
        font=("Noto Sans HK Black", 16)
    )

    label.pack(pady=30)