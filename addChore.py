import tkinter as tk
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

    #Limit chore name to 21 characters because thats the size of the text box
    def limitChoreNameLength(newValue):
        return len(newValue) <= 21

    validateCommand = choreNameEntry.register(limitChoreNameLength)
    choreNameEntry.config(validate="key", validatecommand=(validateCommand, "%P"))

    xpAmountEntry = tk.Entry(root, width=25, font=("Noto Sans HK Black", 12))
    xpAmountEntry.pack(pady=5)
    addPlaceholder(xpAmountEntry, "XP Amount")

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