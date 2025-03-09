"""
    """"""""""""""""""  program to make a legendary calculator  """"""""""""""""""
    """"""""""""""""""          that you just cannot do         """"""""""""""""""
"""

# some verrrry important functions
def about():
    showinfo("About Calculator", "Calculator by Aayush Kumar.\nYou can contact Sir Aayush Kumar by dailing this no 9XXXXXXXXX")

def _help():
    open_new("https://en.wikipedia.org/wiki/Calculator")

def create_a_button(text, padx, foreground, row, column):
    if text == "Del":
        button = Button(
            button_frame,
            text = text,
            padx = padx,
            pady = 8,
            bg = "black",
            fg = foreground,
            activebackground = "black",
            activeforeground = "white",
            bd = 4,
            font = "DS-Digital 15 italic"
        )
        button.grid_configure(row = row, column = column)
        button.bind("<Button-1>", calculate)

    else:
        button = Button(
            button_frame,
            text = text,
            padx = padx,
            bg = "black",
            fg = foreground,
            activebackground = "black",
            activeforeground = "white",
            bd = 4,
            font = "DS-Digital 20 italic"
        )
        button.grid_configure(row = row, column = column)
        button.bind("<Button-1>", calculate)




#########################   MAIN LOGIC BEHIND THE FULL CALCULATOR   #########################
def calculate(event):
    global screen_entry
    global screenFontSize

    scr_text = screen_entry.get()
    text = event.widget.cget("text")

    if text == "Del":
        screen_entry.set(scr_text[:-1])
        screen.update()
        
    elif text == "CE" or text == "C":
        screen_entry.set("")
        screen.update()
        
    elif text == "=":
        try:
            result = eval(screen.get())
            screen_entry.set(result)
            screen.update()
        except:
            screen_entry.set("Error")

    else:
        screen_entry.set(scr_text + text)
        screen.update()




#########################   MAIN LOGIC BEHIND THE FULL CALCULATOR   #########################

if __name__ == "__main__":
    # importings
    from tkinter import *
    from tkinter.messagebox import *
    from webbrowser import open_new

    # some Tk settings
    root = Tk()
    # root.geometry("285x365")
    root.minsize(202, False)
    root.title("Calculator - Ak")
    root.configure(bg = "black")
    # root.resizable(False, False)
    # root.wm_iconbitmap("iconbitmap.ico", "iconbitmap.ico")
    root.iconphoto(True, PhotoImage(file="iconbitmap.png"))

    # menu bar
    main_menu = Menu(root)

    # "window" menu
    m1 = Menu(main_menu, tearoff = 0)
    m1.add_command(label = "Exit", command = root.destroy)
    root.config(menu = main_menu)
    main_menu.add_cascade(label = "Window", menu = m1)

    # "help" menu
    m2 = Menu(main_menu, tearoff = 0)
    m2.add_command(label = "About Calculator", command = about)
    m2.add_separator()
    m2.add_command(label = "Help", command = _help)
    root.config(menu = main_menu)
    main_menu.add_cascade(label = "Help", menu = m2)

    # creating input panel for our calculator
    screen_entry = StringVar()
    screen = Entry(root, text = "0", textvariable = screen_entry, font = "DS-Digital 30 bold")
    screen.pack(ipadx = 5, ipady = 11, fill = X)

    # button frame
    button_frame = Frame(root, bg = "black", bd = 5, relief = GROOVE)
    button_frame.pack(padx = 15, pady = 15)

    # buttons for our calculator
    def create_a_yellow_button(text, row, column):
        create_a_button(text  , 13, "yellow", row, column)

    def create_a_green_button(text, row, column):
        create_a_button(text  , 13, "#00ff00", row, column)

    create_a_button("Del", 7 , "#00ff00" , 0, 0)
    create_a_button("CE" , 7 , "#00ff00" , 0, 1)
    create_a_button("1"  , 16, "yellow", 3, 0)
    create_a_button("."  , 17, "yellow", 4, 0)
    create_a_button("00" , 7 , "yellow", 4, 2)
    
    create_a_yellow_button("7", 1, 0)
    create_a_yellow_button("8", 1, 1)
    create_a_yellow_button("9", 1, 2)
    create_a_yellow_button("4", 2, 0)
    create_a_yellow_button("5", 2, 1)
    create_a_yellow_button("6", 2, 2)
    create_a_yellow_button("2", 3, 1)
    create_a_yellow_button("3", 3, 2)
    create_a_yellow_button("0", 4, 1)

    create_a_green_button("C", 0, 2)

    i = 0
    green_buttons_list = ["/", "*", "-", "+", "="]
    for text in green_buttons_list:
        create_a_green_button(text, i, 3)
        i += 1

    # starting our calculator GUI window
    root.mainloop()
