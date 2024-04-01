from tkinter import *
def LogDataWind(tank_wind):
    rev = ""
    ld_wind = Toplevel(tank_wind)
    ld_wind.title('Log Data')
    ld_wind.geometry('500x500')
    with open(currentFile, "rt") as f:
        logtext = f.readlines()
    for line in reversed(logtext):
        rev += f"{line}\n"
    logtextbox = Label(ld_wind, text=rev)
    logtextbox.grid(row=5, column=1)
    ld_wind.mainloop()
    #returnbutton = Button(ld_wind, text='Close Log', command=lamda: )
