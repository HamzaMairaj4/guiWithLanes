import datetime
def logging_movement(username, direction):
    tdytime = datetime.datetime.now()
    tdy = tdytime.strftime("%x")
    timet = tdytime.strftime("%X")
    username_safe = username.replace(":", "_").replace("/", "_")
    tdy = tdy.replace(":", "_").replace("/", "_")
    timet = timet.replace(":", "_").replace("/", "_")
    print(currentFile)
    f = open(currentFile, "a")
    if direction == 'stop':
        writestr = f"\n{username} stopped the robot on {tdy} at {timet}"
    elif direction == 'logout':
        writestr = f"\n{username} logged out on {tdy} at {timet}"
    else:
        writestr = f"\n{username} moved the robot {direction} on {tdy} at {timet}"

    f.write(writestr)
    f.close()