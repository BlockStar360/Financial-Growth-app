import tkinter as tk

def addPlaceholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(fg="light grey")

    def onFocusIn(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def onFocusOut(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="grey")

    entry.bind("<FocusIn>", onFocusIn)
    entry.bind("<FocusOut>", onFocusOut)