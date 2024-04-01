# if a user logs in successfully, creates the Tank GUI window with,
# #at the moment, a welcome statement and logout button
from all_log import *
from postDataMove import *
from logging_out import *
from LogDataWind import *
import tkinter as tk
from PIL import Image, ImageTk
import cv2 as cv
import numpy as np
from laneDetection import *

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
        def processVideo(p1,p2,p3,p4,cvThresh):
            ret, frame = final_cap.read()
            if ret:
                pts1 = np.float32([p1, p2, p3, p4])
                pts2 = np.float32([[0, 640], [0, 0], [400, 0], [400, 650]])

                # Apply Perspective Transform Algorithm
                matrix = cv.getPerspectiveTransform(pts1, pts2)
                cFrame = cv.warpPerspective(frame, matrix, (400, 650))

                cv.imshow('transfromers', cFrame)

                try:
                    nallo, gallo, mallo = laneDetection(cFrame,cvThresh)
                except:
                    pass

                procFrame = cv.cvtColor(cFrame, cv.COLOR_BGR2GRAY)

                pts = np.array([p1, p2, p3, p4],
                               np.int32)

                pts = pts.reshape((-1, 1, 2))

                isClosed = True

                # Blue color in BGR
                color = (255, 0, 0)

                # Line thickness of 2 px
                thickness = 2

                # Using cv2.polylines() method
                # Draw a Blue polygon with
                # thickness of 1 px
                image = cv.polylines(frame, [pts],
                                      isClosed, color, thickness)
                cFrame = Image.fromarray(cFrame)
                cFrame = ImageTk.PhotoImage(cFrame)
                final_frame.config(image=cFrame)
                final_frame.image = cFrame


        tank_wind = Toplevel(login_wind)
        login_wind.withdraw()
        tank_wind.title('Tank Interface')

        # Welcome label
        welcome = Label(tank_wind, text=f'Welcome {name.title()}')
        welcome.grid(row=0, column=1, pady=10)  # Placing it in the middle top

        video_frame = tk.Label(tank_wind,width=200, height=400)
        video_frame.grid(row=0,column=0,rowspan=1,padx=10,pady=10)
        final_frame = tk.Label(tank_wind,width=60, height = 40)
        final_frame.grid(row=1, column=0,rowspan=200,padx=10,pady=400)

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
        final_cap = cv.VideoCapture('IMG_2555.MOV')
        p1 = [0, 1130]
        # top left
        p2 = [370, 930]
        # top right
        p3 = [720, 930]
        # bottom right
        p4 = [1080, 1130]
        processVideo(p1,p2,p3,p4,120)

        cap = cv.VideoCapture('IMG_2545.MOV')
        updateVideo()
        final_cap = cv.VideoCapture('IMG_2545.MOV')
        # bottom left
        p1 = [20, 1200]
        # top left
        p2 = [390, 1030]
        # top right
        p3 = [590, 1030]
        # bottom right
        p4 = [890, 1200]
        processVideo(p1,p2,p3,p4,98)

        cap = cv.VideoCapture('IMG_2548.MOV')
        updateVideo()
        final_cap = cv.VideoCapture('IMG_2548.MOV')
        # bottom left
        p1 = [00, 1300]
        # top left
        p2 = [300, 1135]
        # top right
        p3 = [720, 1135]
        # bottom right
        p4 = [940, 1300]
        processVideo(p1, p2, p3, p4, 125)

        tank_wind.mainloop()
