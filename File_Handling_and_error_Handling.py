import os

#deleting file if exist, to prevent errors
if os.path.exists("testfile.txt"):
    os.remove("testfile.txt")

#create a file 
file = open("testfile.txt", "x")
file.write("Hello this is a Test")
file.close

#overwrite 
file= open("testfile.txt", "w")
file.write("I overwrtie the first text in this file, just to say i did it!")
file.close

#append to this file
file=open("testfile.txt", "a")
file.write("\n \nHey, I only added this because I can!")
file.close

#read whole file 
file=open("testfile.txt", "r")
for x in file:
    print(x)

#error handling
if os.path.exists("testfilenotexist.txt"):
    os.remove("testfilenotexist.txt")

try:
    file=open("testfilenotexist.txt","r")
except FileNotFoundError:
    print(f"\nfile dont exists!")
#just to have it in here
finally:
    pass

