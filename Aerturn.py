# returns whatever window is inputted back to the root window
def Aeturn(login_wind, root, username=None):
    login_wind.destroy()
    root.deiconify()