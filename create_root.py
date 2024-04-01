from tkinter import *
from create_window import *
from LoginWindow import *
def create_root():
    root = Tk()
    root.geometry("500x500")
    create = Button(root, text='Create Account', command=lambda: create_window(root))
    create.grid(row=0, column=7)
    log = Button(root, text='Login', command=lambda: LoginWindow(root))
    log.grid(row=1, column=7)
    out = Button(root, text='Quit', command=root.destroy)
    out.grid(row=3, column=7)

    root.mainloop()