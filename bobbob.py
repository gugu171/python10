from tkinter import *
from datetime import date
root = Tk()
root.title('GETING START WIT WIDGITS')
root.geometry('400x300')

lbl = Label(text='henlo dere', fg='white', bg='#072F5F', height=1, width = 300)

name_lbl = Label(text='Ful Nem', bg='#3895D3')
name_entry = Entry()

def display():
    name = name_entry.get()
    global message
    message = 'WELKOM TO APLIKATION! \nTUDAY DAT IS:'
    greet = 'Henlo '+name+'\n'
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)
btn = Button(text='BEGAN', command=display, height = 1, bg='#1261AB', fg='white')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()