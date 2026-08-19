import tkinter as tk

from shop import shopPage
from choreList import choresPage


def homePage(root):

    #Settings
    root.title("Home")
    root.geometry("322x581")
    root.resizable(False, False)

    # Money variables
    money = 65
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
    treeImage = tk.PhotoImage(file="tree.png")

    canvas.create_image(
        161,
        220,
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

    #Make a profile button
    profileButton = tk.Button(
        root,
        text="●",
        font=("Arial", 20),
        width=2,
        height=1,
        command=lambda: profilePage(root),
        relief="flat"
    )

    profileButton.place(
        x=10,
        y=10
    )

    #Format the bar at the bottom
    bottomBar = tk.Frame(
        root,
        bg="#EEEEEE",
        height=50
    )

    bottomBar.place(
        x=0,
        y=531,
        width=322,
        height=50
    )

    #Create a shop button
    shopButton = tk.Button(
        bottomBar,
        text="🛒",
        font=("Segoe UI Emoji", 20),
        bg="#EEEEEE",
        relief="flat",
        command=lambda: shopPage(root)
    )

    shopButton.place(
        x=30,
        y=3,
        width=70,
        height=44
    )

    #Create a home button
    homeButton = tk.Button(
        bottomBar,
        text="🏠",
        font=("Segoe UI Emoji", 20),
        bg="#EEEEEE",
        relief="flat",
        command=lambda: homePage(root)
    )

    homeButton.place(
        x=126,
        y=3,
        width=70,
        height=44
    )

    #Create a chores button
    choresButton = tk.Button(
        bottomBar,
        text="☷",
        font=("Arial", 25),
        bg="#EEEEEE",
        relief="flat",
        command=lambda: choresPage(root)
    )

    choresButton.place(
        x=222,
        y=3,
        width=70,
        height=44
    )

def profilePage(root):

    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(
        root,
        text="Profile Page",
        font=("Noto Sans HK Black", 16)
    )

    label.pack(pady=30)