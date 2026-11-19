from tkinter import *
from tkinter import messagebox



root = Tk()
root.geometry("200x200")




def msg():
    messagebox.showwarning('ALIERNT', 'STAHP ITTT! VIRUSIANOPOCALYPSERAMPOCOLYPSEANAPOCOLYPSEWILLHAPPEN IS DERE ON ADA COMPUTRI')


button = Button(root, text='SKAN POUR DA VIRUSIA', command=msg)
button.place(x=40, y=80)

root.mainloop()