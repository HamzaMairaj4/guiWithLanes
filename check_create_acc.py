# if an account is created succesfully, returns to the root window
from logging_create import *
from login import *
from Aerturn import *

def check_create_acc(user, pword, fname, lname, create_wind, root):
    logging_create(user)
    if create_acc(user, pword, fname, lname):
        Aeturn(create_wind, root)