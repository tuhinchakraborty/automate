import os

desktop = os.scandir("/Users/tuhin/Code/code")

for entry in desktop:
    print(entry.name)


os.system('ls -la')
