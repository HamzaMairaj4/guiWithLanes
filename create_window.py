# imports all the necessary libraries
from tkinter import *
from login import *
import requests
import cv2 as cv
from Aerturn import *
from check_create_acc import *
def create_window(root):
    create_wind = Toplevel(root)
    root.withdraw()
    create_wind.title('Create Account')
    create_wind.geometry('500x500')
    user = Label(create_wind, text='Enter your username: ')
    user.grid(row=0, column=0)
    pword = Label(create_wind, text='Enter your password: ')
    pword.grid(row=1, column=0)
    fname = Label(create_wind, text='Enter your first name: ')
    fname.grid(row=2, column=0)
    lname = Label(create_wind, text='Enter your last name: ')
    lname.grid(row=3, column=0)
    e1 = StringVar()
    e2 = StringVar()
    e3 = StringVar()
    e4 = StringVar()
    userent = Entry(create_wind, textvariable=e1, bg="light gray", fg="black")
    userent.grid(row=0, column=1)
    pwordent = Entry(create_wind, textvariable=e2, bg="light gray", fg="black")
    pwordent.grid(row=1, column=1)
    fnament = Entry(create_wind, textvariable=e3, bg="light gray", fg="black")
    fnament.grid(row=2, column=1)
    lnament = Entry(create_wind, textvariable=e4, bg="light gray", fg="black")
    lnament.grid(row=3, column=1)
    enterbutton = Button(create_wind, text='Create',
                         command=lambda: check_create_acc(userent.get(), pwordent.get(), fnament.get(), lnament.get(),
                                                          create_wind, root))
    enterbutton.grid(row=7, column=0)
    backbutton = Button(create_wind, text='Back', command=lambda: Aeturn(create_wind, root))
    backbutton.grid(row=7, column=1)
    create_wind.mainloop()