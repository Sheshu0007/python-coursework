try:
    file=open("demo1.txt","r")
except FileNotFoundError:
    print("file is not present")
else:
    read=file.read()
    file.seek(0)
    readlines=file.readlines()
    file.seek(0)
    readline=file.readline()
    print(read)
    print(readlines)
    print(readline)
#write mode
try:
    file=open("demo.txt","w")
except FileNotFoundError:
    print("")

#append mode
try:
    file=open("demo.txt","a")
except FileNotFoundError:
    print("File is not presnt")
else:
    file.write("no presentation for sheshu")
    file.seek(0)
    print(read)
    file.close()
finally:
    print("end of the program")
 
# to create a folder
import os
print(os.getcwd)
if not os.path.exists("demo"):
    os.mkdir("demo")

#to remove the folder
import os

if  os.path.exists("demo"):
    os.rmdirr("demo")


#to create subfolder
import os

if not os.path.exists("demo"):
    os.mkdir("demo")
    os.makedirs("demo/1432")

#to remove the 
import os
import shutil
if not os.path.exits("1432"):
    os.mkdir("ds")
    os.makedirs("df/ff")
#os.rmdir("1432/ds")
shutil.rmtree("ds")
