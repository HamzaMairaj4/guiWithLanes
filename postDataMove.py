# imports all the necessary libraries
from tkinter import *
from login import *
import requests
import cv2 as cv
from logging_movement import *

def postDataMove(direct, user):
    url = "http://192.168.1.42:4200/moving"
    data = {'button': direct}
    r = requests.post(url, json=data)
    print("Command Sent")
    logging_movement(user, direct)