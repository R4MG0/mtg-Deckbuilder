import os
import platform

cmd = "python"
if(platform.system() != "Windows"): cmd += "3"


os.system(f"{cmd} createUserDatabase.py")
os.system(f"{cmd} backend.py")