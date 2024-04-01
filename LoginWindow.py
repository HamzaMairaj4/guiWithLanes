from tkinter import *
from check_logged_in import *
from Aerturn import *

def LoginWindow(root):
    login_wind = Toplevel(root)
    root.withdraw()

    login_wind.title('Login')
    login_wind.geometry('500x500')
    user = Label(login_wind, text='Enter your username: ')
    user.grid(row=0, column=0)
    pword = Label(login_wind, text='Enter your password: ')
    pword.grid(row=1, column=0)
    e1 = StringVar()
    e2 = StringVar()
    userent = Entry(login_wind, textvariable=e1, bg="light gray", fg="black")
    userent.grid(row=0, column=1)
    pwordent = Entry(login_wind, textvariable=e2, bg="light gray", fg="black")
    pwordent.grid(row=1, column=1)
    print(userent.get(), pwordent.get())
    enterbutton = Button(login_wind, text='Login',
                         command=lambda: check_logged_in(userent.get(), pwordent.get(), login_wind, root))
    enterbutton.grid(row=5, column=0)
    backbutton = Button(login_wind, text='Back', command=lambda: Aeturn(login_wind, root))
    backbutton.grid(row=5, column=1)
    login_wind.mainloop()