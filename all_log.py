import datetime
def all_log(username):
  tdytime = datetime.datetime.now()
  tdy = tdytime.strftime("%x")
  timet = tdytime.strftime("%X")

  file_time = timet

  file_tdy = tdy

  username_safe = username.replace(":", "_").replace("/", "_")
  tdy = tdy.replace(":", "_").replace("/", "_")
  timet = timet.replace(":", "_").replace("/", "_")

  global currentFile
  currentFile = f"{username}-{tdy}-{timet}.txt"
  print(currentFile)
  f = open(currentFile, "a")
  writestr = f'\n{username} logged into their account'
  f.write(writestr)
  f.close()
  f = open('currentName','w')
  f.write(currentFile)
  f.close()