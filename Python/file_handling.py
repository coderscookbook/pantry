open(filename, mode)
# Modes: r, a, w, x plus binary (b) or text (t) mode

# default
# open("demo_file.txt") is the same as -> open("demo_file.txt", "rt")

# location
f = open("D:\\myfiles\demo_file.txt")
print(f.read())
print(f.read(5)) # specificy how many characters to return
print(f.readline()) 

for x in f:
  print(x)
f.close()

# remove file 
import os
# os.remove("demo_file.txt")
if os.path.exists("demo_file.txt"):
  os.remove("demo_file.txt")
else:
  print("The file does not exist")

# remove folder/directory
os.rmdir("myfolder") # you can only remove empty folders!!


