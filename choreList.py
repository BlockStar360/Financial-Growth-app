import tkinter as tk

from bottomBar import createBottomBar

def choresPage(root):

    for widget in root.winfo_children():
        widget.destroy()

    #Canvas
    canvas = tk.Canvas(
        root,
        width=322,
        height=581,
        bg="white",
        highlightthickness=0
    )

    canvas.pack()

    canvas.create_text(
    161,
    100,
    text="Chores Page",
    font=("Noto Sans HK Black", 16)
)

    createBottomBar(root)