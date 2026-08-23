import tkinter as tk
import os
import session

from shop import shopPage
from choreList import choresPage
from bars import createBottomBar, createTopBar
from database import getXP, getTreeLevel, getSkinOwnership


def homePage(root):

    for widget in root.winfo_children():
            widget.destroy()
    
    #Page settings
    root.title("Home")
    root.geometry("322x581")
    root.resizable(False, False)

    #XP and tree level variables with fallbacks
    childUsername = session.currentUsername
    xp = getXP(session.currentUsername) if session.currentUsername else 0
    maxXP = 100
    treeLevel = getTreeLevel(childUsername) if childUsername else 1
    _, selectedSkin = getSkinOwnership(childUsername) if childUsername else ({}, "default")

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



    #Create the tree graphic
    skinImageFiles = {
    "default": ("big default.png", 270),
    "fire": ("big on fire.png", 225),
    "glitch": ("big glitched.png", 270),
    "galaxy": ("big galaxy.png", 252)
    }

    treeImageFiles = {
        1: ("small.png", 335),
        2: ("medium.png", 297),
        3: skinImageFiles[selectedSkin]
    }

    treeFilename, treeY = treeImageFiles[treeLevel]

    treeImage = tk.PhotoImage(
    file=os.path.join(BASE_DIR, "Tree Graphics", treeFilename)
    )

    canvas.create_image(
        161,
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

    createTopBar(root, "Home page")
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