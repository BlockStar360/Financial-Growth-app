import tkinter as tk

def createTopBar(root, pageTitle):
    #Format the bar at the top
    topBar = tk.Frame(
        root,
        bg="#EEEEEE",
        height=50
    )

    topBar.place(
        x=0,
        y=0,
        width=322,
        height=50
    )

    #Divider line below the top bar
    dividerLine = tk.Frame(
        root,
        bg="#CCCCCC",
        height=2
    )

    dividerLine.place(
        x=0,
        y=50,
        width=322,
        height=2
    )

    #Page title text
    titleLabel = tk.Label(
        topBar,
        text=pageTitle,
        font=("Noto Sans HK Black", 14),
        bg="#EEEEEE"
    )

    titleLabel.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

def createBottomBar(root):
    from shop import shopPage
    from choreList import choresPage
    from homepage import homePage

    #Create the grey divider line to seperate the bottom bar from the rest of the page
    dividerLine = tk.Frame(
        root,
        bg="#CCCCCC",
        height=2
    )

    dividerLine.place(
        x=0,
        y=529,
        width=322,
        height=2
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

    #Create a circle home button
    homeButton = tk.Canvas(
        root,
        width=70,
        height=70,
        highlightthickness=0
    )

    homeButton.place(
        x=126,
        y=511
    )

    #Colour the background to blend in with what's behind it
    homeButton.create_rectangle(0, 0, 70, 20, fill="white", outline="")
    homeButton.create_rectangle(0, 20, 70, 70, fill="#EEEEEE", outline="")

    #Fix the divider line
    homeButton.create_rectangle(0, 18, 70, 20, fill="#CCCCCC", outline="")

    #Green circle for the button
    homeButton.create_oval(
        2,
        2,
        68,
        68,
        fill="#4B8F43",
        outline="#1F5019",
        width=3
    )

    #Add an emoji
    homeButton.create_text(
        35,
        35,
        text="🌳",
        font=("Segoe UI Emoji", 25)
    )

    homeButton.bind(
        "<Button-1>",
        lambda event: homePage(root)
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