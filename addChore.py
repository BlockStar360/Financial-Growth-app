import tkinter as tk
import tkinter.font as tkfont
from functions import showPopup, addPlaceholder, getRealValue
from database import addChore


def handleChoreSubmit(choreName, xpAmountText, childUsername, root):
    if not choreName or not xpAmountText:
        showPopup(root, "Error", "Please fill out both fields")
        return

    try:
        xpAmount = int(xpAmountText)
    except ValueError:
        showPopup(root, "Error", "XP amount must be a number")
        return

    addChore(childUsername, choreName, xpAmount)

    from choreList import choresPage
    choresPage(root)


#Create the add chore window
def addChorePage(root, childUsername):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Add Chore")
    root.geometry("300x550")
    root.resizable(False, False)

    label = tk.Label(root, text="Add a Chore", font=("Noto Sans HK Black", 12))
    label.pack(pady=10)

    choreNameEntry = tk.Entry(root, width=25, font=("Noto Sans HK Black", 12))
    choreNameEntry.pack(pady=5)
    addPlaceholder(choreNameEntry, "Chore Name")

    #Stops the user from typing when they reach the end of the box
    entryFont = tkfont.Font(font=("Noto Sans HK Black", 12))

    def limitChoreNameLength(newValue):
        maxPixelWidth = choreNameEntry.winfo_reqwidth() - 5
        return entryFont.measure(newValue) <= maxPixelWidth

    validateCommand = choreNameEntry.register(limitChoreNameLength)
    choreNameEntry.config(validate="key", validatecommand=(validateCommand, "%P"))

    xpAmountEntry = tk.Entry(root, width=25, font=("Noto Sans HK Black", 12))
    xpAmountEntry.pack(pady=5)
    addPlaceholder(xpAmountEntry, "XP Amount")

    #Only lets the user type 3 numbers for the XP amount
    def limitXPInput(newValue):
        if newValue == "":
            return True
        return newValue.isdigit() and len(newValue) <= 3

    xpValidateCommand = xpAmountEntry.register(limitXPInput)
    xpAmountEntry.config(validate="key", validatecommand=(xpValidateCommand, "%P"))

    submitButton = tk.Button(root,
                            text="Submit",
                            command=lambda: handleChoreSubmit(
                                getRealValue(choreNameEntry),
                                getRealValue(xpAmountEntry),
                                childUsername,
                                root
                            ),
                            font=("Noto Sans HK Black", 12)
                            )
    submitButton.pack(pady=10)