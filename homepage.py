import tkinter as tk
import os

from shop import shopPage
from choreList import choresPage
from bottomBar import createBottomBar


def homePage(root):

    for widget in root.winfo_children():
            widget.destroy()
    
    #Page settings
    root.title("Home")
    root.geometry("322x581")
    root.resizable(False, False)

    # Money variables
    money = 25
    maxMoney = 100

    #Canvas
    canvas = tk.Canvas(
        root,
        width=322,
        height=581,
        bg="white",
        highlightthickness=0
    )

    canvas.pack()

    #Create the tree graphic
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    treeImage = tk.PhotoImage(
    file=os.path.join(BASE_DIR, "Tree Graphics", "big default.png")
    )

    canvas.create_image(
        161,
        227,
        image=treeImage
    )
    canvas.treeImage = treeImage

    #Money progress bar stuff
    barX1 = 60
    barY1 = 360
    barX2 = 262
    barY2 = 395

    #Create an outline for the money progress bar
    canvas.create_rectangle(
        barX1,
        barY1,
        barX2,
        barY2,
        fill="white",
        outline="#4B8F43",
        width=8
    )

    #Money progress bar for tree upgrade
    moneyPercentage = min(money / maxMoney, 1)
    fillWidth = (barX2 - barX1) * moneyPercentage
    canvas.create_rectangle(
        barX1 + 4,
        barY1 + 4,
        barX1 + 4 + fillWidth,
        barY2 - 4,
        fill="#FFD83D",
        outline=""
    )

    createBottomBar(root)

def profilePage(root):

    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(
        root,
        text="Profile Page",
        font=("Noto Sans HK Black", 16)
    )

    label.pack(pady=30)