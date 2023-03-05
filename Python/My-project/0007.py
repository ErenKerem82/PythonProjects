from tkinter import *
import tkinter
from tkinter import ttk


pencere = Tk()
canva = Canvas(pencere, width=500, height=300)
canva.pack()

name = Label()
name.config(text="Name : ")
name.place(relx=0.3, rely=0.1)

entry = Entry()
entry.place(relx=0.4, rely=0.1)

surname = Label()
surname.config(text="Id : ")
surname.place(relx=0.3, rely=0.2)

entry1 = Entry()
entry1.place(relx=0.4, rely=0.2)

kurum = Label()
kurum.config(text="corporation  :")
kurum.place(relx=0.2, rely=0.3)


hack = ttk.Combobox(
    pencere, values=["NASA", "CİA", "FBI", "MİT", "İNTERPOL", "TESLA", "SPACEX", "NSA", "KGB", "MOSSAD", "RAW", "MSS", "FSB", "MI6 -SIS"])
hack.place(relx=0.4, rely=0.3)

ara = Button()
ara.config(text="SEARCH", background="Black", fg="White",
           borderwidth=8, font="verdana 12 bold")
ara.place(relx=0.3, rely=0.5, relheight=0.2, relwidth=0.3)

mainloop()
