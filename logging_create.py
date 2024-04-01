import datetime
def logging_create(username):
    try:
        tdytime = datetime.datetime.now()
        tdy = tdytime.strftime("%x")
        timet = tdytime.strftime("%X")

        # Replace invalid characters in the filename
        username_safe = username.replace(":", "_").replace("/", "_")
        tdy = tdy.replace(":", "_").replace("/", "_")
        timet = timet.replace(":", "_").replace("/", "_")

        fileName = f"{username_safe}-{tdy}-{timet}.txt"

        writestr = f"\n{username} created an account on {tdy} at {timet}"

        with open(fileName, "w") as f:
            f.write(writestr)

    except Exception as e:
        print(f"An error occurred: {e}")