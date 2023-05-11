import os
import threading
import platform

cmd = "python"
if(platform.system() != "Windows"): cmd += "3"

os.system(f'{cmd} createstorage.py')
os.system(f'{cmd} createruntime.py')


os.system(f"{cmd} backend.py & {cmd} import.py")
