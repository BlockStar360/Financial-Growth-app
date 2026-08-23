import tkinter as tk

#Create text that goes in the login text fields when they're empty
def addPlaceholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(fg="light grey")
    entry.isPlaceholder = True

    def onFocusIn(event):
        if entry.isPlaceholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")
            entry.isPlaceholder = False

    def onFocusOut(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="grey")
            entry.isPlaceholder = True

    entry.bind("<FocusIn>", onFocusIn)
    entry.bind("<FocusOut>", onFocusOut)

#Checks if the text box is has actual text or just the placeholder
def getRealValue(entry):
    return "" if getattr(entry, "isPlaceholder", False) else entry.get().strip()

#Make a popup screen with custom text
def showPopup(root, title, message):
    popupFrame = tk.Frame(
        root,
        bg="white",
        bd=2,
        relief="solid"
    )

    popupFrame.place(
        relx=0.5,
        rely=0.5,
        anchor="center",
        width=250,
        height=150
    )

    #Creates a header for the popup
    titleLabel = tk.Label(
        popupFrame,
        text=title,
        font=("Noto Sans HK Black", 12),
        bg="white"
    )
    titleLabel.pack(pady=(20, 5))

    #Creates text on the popup
    messageLabel = tk.Label(
        popupFrame,
        text=message,
        font=("Noto Sans HK Black", 10),
        bg="white"
    )
    messageLabel.pack()

    #Button to close the popup message
    closeButton = tk.Button(
        popupFrame,
        text="Close",
        command=popupFrame.destroy,
        font=("Noto Sans HK Black", 10)
    )
    closeButton.pack(pady=10)