import os
import platform
# from threading import Thread
# If multiple clients needed probably someday necessary
cmd = "python"
# change "python" to python3 if on linux
if(platform.system() != "Windows"): cmd += "3"

# create dbs, realtive simple

def createStorage():
    os.system(f"{cmd} createstorage.py")
def createRuntime():
    os.system(f"{cmd} createruntime.py")

def createBackend():
    # backend.py is all backend functions in one file, could be made cleaner but should work
    os.system(f"{cmd} backend.py")

createStorage()
createRuntime()
createBackend()
