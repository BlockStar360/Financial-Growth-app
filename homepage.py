import tkinter as tk
import os
import session

from shop import shopPage
from choreList import choresPage
from bars import createBottomBar, createTopBar
from database import getXP, getTreeLevel, getSelectedSkin, sellTree


def homePage(root):

    for widget in root.winfo_children():
            widget.destroy()
    
    #Page settings
    root.title("Home")
    root.geometry("322x581")
    root.resizable(False, False)

    #XP and tree level variables with fallbacks
    childUsername = session.currentUsername
    xp = getXP(childUsername) if childUsername else 0
    maxXP = 100
    treeLevel = getTreeLevel(childUsername) if childUsername else 0
    selectedSkin = getSelectedSkin(childUsername) if childUsername else "default"

    #Stores the amount of money that each skin sells for
    sellAmounts = {
    "default": 100,
    "fire": 150,
    "glitch": 200,
    "galaxy": 300
    }

    #Trees are only sellable at max level and XP
    isSellable = (treeLevel == 3 and xp >= maxXP)

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



    #Create the tree graphic or not if the user doesn't have a tree
    if treeLevel == 0:
        canvas.create_text(
            161,
            290,
            text="Buy a tree in the shop",
            font=("Noto Sans HK Black", 12),
            fill="black",
            justify="center"
        )
    else:
        defaultImages = {
        1: ("small default.png", 161, 335),
        2: ("medium default.png", 161, 297),
        3: ("big default.png", 161, 270)
        }

        fireImages = {
            1: ("small on fire.png", 161, 285),
            2: ("medium on fire.png", 161, 265),
            3: ("big on fire.png", 161, 225)
        }

        glitchImages = {
            1: ("small glitched.png", 161, 335),
            2: ("medium glitched.png", 161, 297),
            3: ("big glitched.png", 161, 270)
        }

        galaxyImages = {
            1: ("small galaxy.png", 161, 350),
            2: ("medium galaxy.png", 173, 310),
            3: ("big galaxy.png", 161, 252)
        }

        #Stores 4 groups of 3 images
        skinImageSets = {
        "default": defaultImages,
        "fire": fireImages,
        "glitch": glitchImages,
        "galaxy": galaxyImages
        }

        treeFilename, treeX, treeY = skinImageSets[selectedSkin][treeLevel]

        treeImage = tk.PhotoImage(
        file=os.path.join(BASE_DIR, "Tree Graphics", treeFilename)
        )

        canvas.create_image(
            treeX,
            treeY, #Y position of tree, higher number = lower on the page
            image=treeImage
        )
        canvas.treeImage = treeImage

    #XP progress bar stuff
    barX1 = 60
    barY1 = 360
    barX2 = 262
    barY2 = 395

    #Create an outline for the XP progress bar
    canvas.create_rectangle(
        barX1,
        barY1,
        barX2,
        barY2,
        fill="white",
        outline="#4B8F43",
        width=8
    )

    #XP progress bar increasing for leveling up the tree
    #Finding the width of the inside of the bar
    innerX1 = barX1 + 4
    innerX2 = barX2 - 4
    innerWidth = innerX2 - innerX1

    if isSellable:
        sellAmount = sellAmounts[selectedSkin]

        #Make the bar into a clickable button with text that says the amount of money you get for sell
        barTag = "sellBar"
        canvas.create_rectangle(
            innerX1,
            barY1 + 4,
            innerX2,
            barY2 - 4,
            fill="#FFD83D",
            outline="",
            tags=barTag
        )

        #Create the sell amount text
        canvas.create_text(
            161,
            (barY1 + barY2) / 2,
            text=f"Sell +${sellAmount}",
            font=("Noto Sans HK Black", 12, "bold"),
            fill="white",
            tags=barTag
        )

        def handleSellTree():
            sellTree(childUsername, sellAmount)
            #Refresh the page
            homePage(root)

        canvas.tag_bind(barTag, "<Button-1>", lambda event: handleSellTree())

    else:
        #Filling the inside of the bar not the outline
        moneyPercentage = min(xp / maxXP, 1)
        fillWidth = innerWidth * moneyPercentage

        canvas.create_rectangle(
            innerX1, 
            barY1 + 4, 
            innerX1 + fillWidth, 
            barY2 - 4, 
            fill="#FFD83D", 
            outline=""
        )

    #Create the XP amount text
    canvas.create_text(
    161,
    barY2 + 15,
    text=f"{xp}/{maxXP} XP",
    font=("Noto Sans HK Black", 10),
    fill="black"
    )

    #Create the tree level text
    levelText = "Lv. MAX" if treeLevel == 3 else f"Lv. {treeLevel}"
    canvas.create_text(
        161,
        barY2 + 32,
        text=levelText,
        font=("Noto Sans HK Black", 10),
        fill="black"
    )

    createTopBar(root, "Home")
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