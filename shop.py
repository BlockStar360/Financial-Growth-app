import tkinter as tk
import os
import session

from bars import createBottomBar, createTopBar
from database import getMoney, spendMoney, hasActiveTree, plantTree
from functions import showPopup

def shopPage(root):

    for widget in root.winfo_children():
        widget.destroy()

    #Page settings
    root.title("Shop")
    root.geometry("322x581")
    root.resizable(False, False)
    
    #Canvas
    canvas = tk.Canvas(
        root,
        width=322,
        height=581,
        bg="white",
        highlightthickness=0
    )

    canvas.pack()

    #Create the background
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    backgroundImage = tk.PhotoImage(
    file=os.path.join(BASE_DIR, "Tree Graphics", "app background.png")
    )

    canvas.create_image(
        161,
        290,
        image=backgroundImage
    )
    canvas.bgImage = backgroundImage

    #Gets the users money amount from the database
    childUsername = session.currentUsername
    money = getMoney(childUsername) if childUsername else 0

    #Stores the display names, actual names (keys) and price for each skin
    skins = [
        ("Default", "default", 0),
        ("Glitch", "glitch", 100),
        ("Fire", "fire", 200),
        ("Galaxy", "galaxy", 300)
    ]

    nextY = 75

    #Plant a new tree of a certain skin if the user doesn't already have a tree
    def handleSkinClick(skinKey, price):
        if hasActiveTree(childUsername):
            showPopup(root, "Can't buy tree yet", "Grow your current tree first!")
            return

        if price > 0 and not spendMoney(childUsername, price):
            showPopup(root, "Not enough money", "You're broke buddy")
            return

        plantTree(childUsername, skinKey)
        #Refresh the page
        shopPage(root)

    for displayName, skinKey, price in skins:
        tag = f"skin_{skinKey}"

        canvas.create_rectangle(
            20, nextY - 15,
            302, nextY + 15,
            fill="white",
            outline="#4B8F43",
            width=2,
            tags=tag
        )

        canvas.create_text(
            35, nextY,
            text=displayName,
            font=("Noto Sans HK Black", 11),
            anchor="w",
            tags=tag
        )

        rightText = "Free" if price == 0 else f"${price}"

        canvas.create_text(
            287, nextY,
            text=rightText,
            font=("Noto Sans HK Black", 11),
            anchor="e",
            tags=tag
        )

        canvas.tag_bind(
            tag,
            "<Button-1>",
            lambda event, key=skinKey, p=price: handleSkinClick(key, p)
        )

        nextY += 40

    #Create the money amount text
    canvas.create_text(
        161,
        nextY,
        text=f"You have ${money}",
        font=("Noto Sans HK Black", 13),
        fill="black"
    )

    createTopBar(root, "Shop")
    createBottomBar(root)