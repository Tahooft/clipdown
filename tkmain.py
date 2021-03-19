# Importing Tkinter and Ttk
import tkinter as tk
from tkinter import ttk

# Create the window
root = tk.Tk()
root.title('Azure')

# Place the window in the center of the screen
windowWidth = 800
windowHeight = 530
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
xCordinate = int((screenWidth/2) - (windowWidth/2))
yCordinate = int((screenHeight/2) - (windowHeight/2))
root.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight,
                                   xCordinate, yCordinate))

# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call('source', 'themes/azure-dark.tcl')

# Set the theme with the theme_use method
style.theme_use('azure-dark')


# Button function
def button_function():
    print('Button callback')


# Button
button = ttk.Button(root, text='Button', command=button_function)
button.place(x=250, y=320)

# Sizegrip
sizegrip = ttk.Sizegrip(root)
sizegrip.place(x=780, y=510)


root.mainloop()
