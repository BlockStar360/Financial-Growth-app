import tkinter as tk
import os
import session

from parentLogin import parentLoginPage
from bars import createBottomBar, createTopBar
from database import getChoresFor, deleteChore, addXP

def choresPage(root):

    for widget in root.winfo_children():
        widget.destroy()

    #Page settings
    root.title("Chores")
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

    #Keep track of the highest available y position for chore boxes
    nextY = 75

    childUsername = session.currentUsername
    chores = getChoresFor(childUsername) if childUsername else []

    #Keeps track of the y positions of chore boxes to replace them with flash text
    choreYPositions = {}

    def completeChore(choreId, xpAmount, tag):
        #Makes the box unclickable
        canvas.tag_unbind(tag, "<Button-1>")

        #Remove the original box to display the XP amount
        canvas.delete(tag)

        y = choreYPositions[choreId]
        canvas.create_rectangle(
            20, y - 15,
            302, y + 15,
            fill="#FFD83D",
            outline="#4B8F43",
            width=2
        )
        canvas.create_text(
            161, y,
            text=f"+{xpAmount} XP",
            font=("Noto Sans HK Black", 12, "bold"),
            fill="black"
        )

        #After one second, remove the box and add XP
        def finishChore():
            addXP(childUsername, xpAmount)
            deleteChore(choreId)
            choresPage(root)

        root.after(1000, finishChore)

    for choreId, choreName, xpAmount in chores:
        tag = f"chore_{choreId}"
        choreYPositions[choreId] = nextY #Save the y position of this chore

        #Create the box outline
        canvas.create_rectangle(
            20, nextY - 15,
            302, nextY + 15,
            fill="white",
            outline="#4B8F43",
            width=2,
            tags=tag
        )

        #Chore name on the left
        canvas.create_text(
            35, nextY,
            text=choreName,
            font=("Noto Sans HK Black", 11),
            anchor="w",
            tags=tag
        )

        #XP amount on the right
        canvas.create_text(
            287, nextY,
            text=f"{xpAmount} XP",
            font=("Noto Sans HK Black", 11),
            anchor="e",
            tags=tag
        )

        #Makes each box individual so they can be clicked
        canvas.tag_bind(
            tag,
            "<Button-1>",
            lambda event, cid=choreId, xp=xpAmount, t=tag: completeChore(cid, xp, t)
        )

        #Make it so that the next box stacks without overlapping
        nextY += 40

    parentButton = tk.Button(
        canvas,
        text="Add a chore",
        command=lambda: parentLoginPage(root),
        font=("Noto Sans HK Black", 12)
    )
    canvas.create_window(161, nextY, window=parentButton)

    createTopBar(root, "Chores list")
    createBottomBar(root)