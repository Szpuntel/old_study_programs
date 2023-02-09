# copyfile() = copies content of a file
# copy() = copyfile() + permission mod + destination can be a directory
# copy2() = copy() + copies meatadata (file'screation and modification times)


import shutil

shutil.copyfile('test.txt','copy.txt') #src.dst rafa