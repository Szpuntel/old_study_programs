import os

path = "C:\\Users\\szpun\\Desktop\\foot.jpg"

if os.path.exists(path):
    print("Dat locatione exists")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("that is a dictionary")
else:
    print("No Dat location doesnt exists")