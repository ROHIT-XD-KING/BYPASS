import os
import platform
print("JOIN FB GROUP")
os.system("xdg-open https://facebook.com/groups/460389902592352/")
os.system("git pull")
try:
    __import__("SPYVIP").Spy()
except Exception as e:
    exit(str(e))
