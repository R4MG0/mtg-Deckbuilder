import os
import platform
from threading import Thread
# If multiple clients needed probably someday necessary
cmd = "python"
# change "python" to python3 if on linux
if(platform.system() != "Windows"): cmd += "3"


def newThread(func):
    t = Thread(target=func)
    t.start()

# create dbs, realtive simple

def createStorage():
    os.system(f"{cmd} createstorage.py")
def createRuntime():
    os.system(f"{cmd} createruntime.py")

def createBackend():
    # backend.py is all backend functions in one file, could be made cleaner but should work
    os.system(f"{cmd} backend.py")
def createWSServer():
    # creates a handler for the websockets
    # was developed in /ws so if any problems
    # rise, Experiment there
    os.system(f"{cmd} websocketsserver.py")

createStorage()
createRuntime()
newThread(createBackend)
newThread(createWSServer)

