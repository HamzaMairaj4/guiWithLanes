# if a user logs in successfully, creates the Tank GUI window with,
# #at the moment, a welcome statement and logout button
from all_log import *
from login import *
from tkinter import *
from postDataMove import *
from logging_out import *
from LogDataWind import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
def check_logged_in(user, password, login_wind, root):
    all_log(user)
    f = open('currentName','r')
    currentFile = f.read()
    f.close()
    f=open(currentFile,"r")
    timber = f.read()
    f.close()
    valid, name = login(user, password)
    if valid:
        # tank_wind = Toplevel(login_wind)
        # login_wind.withdraw()
        # tank_wind.title('Tank Interface')
        #
        # welcome = Label(tank_wind, text=f'Welcome {name.title()}')
        # logout = Button(tank_wind, text='Logout', command=lambda: logging_out(tank_wind, root, user))
        # viewlog = Button(tank_wind, text='View Full Log', command=lambda: LogDataWind(tank_wind))
        # forward = Button(tank_wind, text=u'\u2191', command=lambda: postDataMove("forward", user))
        # backward = Button(tank_wind, text=u'\u2193', command=lambda: postDataMove("backward", user))
        # right = Button(tank_wind, text=u'\u2192', command=lambda: postDataMove("right", user))
        # left = Button(tank_wind, text=u'\u2190', command=lambda: postDataMove("left", user))
        # play = Button(tank_wind, text=u'\u25B6', command=lambda: postDataMove("go", user))
        # stop = Button(tank_wind, text=u'\u2587', command=lambda: postDataMove("stop", user))
        def updateVideo():
            ret, frame = cap.read()
            if ret:
                frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                frame = Image.fromarray(frame)
                frame = ImageTk.PhotoImage(frame)
                video_frame.config(image=frame)
                video_frame.image = frame
            tank_wind.after(10, updateVideo)

        tank_wind = Toplevel(login_wind)
        login_wind.withdraw()
        tank_wind.title('Tank Interface')

        # Welcome label
        welcome = Label(tank_wind, text=f'Welcome {name.title()}')
        welcome.grid(row=0, column=1, pady=10)  # Placing it in the middle top

        video_frame = tk.Label(tank_wind)
        video_frame.grid(row=0,column=0,rowspan=4,padx=10,pady=10)

        # Frame for buttons
        button_frame = Frame(tank_wind)
        button_frame.grid(row=1, column=2, padx=10, pady=10)

        # Buttons
        forward = Button(button_frame, text=u'\u2191', command=lambda: postDataMove("forward", user))
        backward = Button(button_frame, text=u'\u2193', command=lambda: postDataMove("backward", user))
        right = Button(button_frame, text=u'\u2192', command=lambda: postDataMove("right", user))
        left = Button(button_frame, text=u'\u2190', command=lambda: postDataMove("left", user))
        play = Button(button_frame, text=u'\u25B6', command=lambda: postDataMove("go", user))
        stop = Button(button_frame, text=u'\u2587', command=lambda: postDataMove("stop", user))

        # Grid placements for buttons within the frame
        forward.grid(row=0, column=1)
        backward.grid(row=2, column=1)
        right.grid(row=1, column=2)
        left.grid(row=1, column=0)
        play.grid(row=1, column=1)
        stop.grid(row=1, column=1)

        # Log Button
        viewlog = Button(tank_wind, text='View Full Log', command=lambda: LogDataWind(tank_wind))
        viewlog.grid(row=3, column=2, sticky='sw', padx=10, pady=10)  # Placing in bottom left

        # Logout Button
        logout = Button(tank_wind, text='Logout', command=lambda: logging_out(tank_wind, root, user))
        logout.grid(row=0, column=2, sticky='nw', padx=10, pady=10)  # Placing in top left

        # log_data = Button(tank_wind, text='View Full Log', command=lambda: postData("stop", user))
        # tank_wind.bind('<Up>', lambda: postDataMove('forward', user))
        # tank_wind.bind('<Down>', lambda: postDataMove('backward', user))
        # tank_wind.bind('<Left>', lambda: postDataMove('left', user))
        # tank_wind.bind('<Right>', lambda: postDataMove('right', user))
        cap = cv.VideoCapture('IMG_2555.MOV')
        updateVideo()

        tank_wind.mainloop()
