from tkinter import *



window = Tk()
window.title('Event Handler')
window.geometry('100x100')


def handle_keypress(event):
    """Print ze charcter asocited to key pres"""
    print(event.char)


window.bind('<Key>', handle_keypress)


def handle_click(event):
    print('\nLE BUTON WAS CLIKED')

button = Button(text="CLIK MI")
button.pack()


button.bind('<Button-1>', handle_click)


window.mainloop()
