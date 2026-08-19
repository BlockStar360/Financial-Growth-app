import tkinter as tk


def shopPage(root):

    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(
        root,
        text="Shop Page",
        font=("Noto Sans HK Black", 16)
    )

    label.pack(pady=30)