# https://medium.com/@shekharvrm47/how-i-improved-my-python-code-performance-by-371-ea6209b9ab61

# KEY CONCEPTS: loop invariance, 

# SCENARIO: 1. csv with 46.66M rows (1.11GB)
#           2. extract only rows for a gien value of the third column (3100.10)
#           3. write rows to a new csv ("result.txt")
# SAMPLE ROWS:  1 0 3098 3100.10 54188
#               2 7 3098 3100.10 38293
#               3 9 3482 2222.83 54188

# FIRST ITERATION: use numpy.genfromtxt()
#   - gave memory error -> data too big to handle at once
#   - tried to segment data into smaller chunks -> painfully slow

# Basic Approach (29.3s +- 56.7ms/loop)
def Function(file):
  output      = "result.txt"
  output_file = open(output, "w")
  value       = int(3100.10)
  
  with open(file, "r") as f:
    for line in f:
      if(line != "\n"):
        if(len(line.split(" ")) == 4):
          try:
            if(int(float(line.split(" ")[2])) == int(value)):
              output_file.write(line)
          except ValueError:
            continue
  f.close()
  output_file.close()


# FIRST ITERATION (27.5s +- 264ms/loop => 6.5% increase speed from Basic)
# Loop Invariance Fix
# en.wikipedia.org/wiki/Loop_invariant
# - Step 1: look for unecessary code
#   - using int(value) in loop to compare the value
#   - instead, convert value to an int once and use it in the loop ("Loop Invariance")
#   - Loop Invariance = when we do something in the loop again and again, but avoidable
def Function1(file):
  output      = "result.txt"
  output_file = open(output, "w")
  value       = int(3100.10)

  with open(file, "r") as f:
    for line in f:
      if(line != "\n"):
        if(len(line.split(" ")) == 4):
          try:
            if(int(float(line.split(" ")[2])) == value):
              output_file.write(line)
          except ValueError:
            continue
  f.close()
  output_file.close()


# SECOND ITERATION (22.8s +- 124ms/loop => 20% increase from 1st It.)  
# Memory Mapping the File
# https://realpython.com/python-mmap/#search-a-memory-mapped-file
# - load enter file into memory (RAM = faster than file IO) 
# - Conventional IO uses multiple system calls to read data from the disk and get it back to the program via multiple data buffers 
# - Memory mapping skips these steps and copies the data to memory = improved performance (in most cases) 
# - Python has module named "mmap" 
# - Line79: slicing the row to get 3rd element then converting the string to float and then to int to do comparison ("1 0 3098 3100.10 54188" => "3100.10" => 3100.10 => 3100)
import mmap
def Function2(file):
  output      = "result.txt"
  output_file = open(output, "w")
  value       = int(3100.10)
  
  with open(file, "r+b") as f:
    mmap_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    for line in iter(mmap_file.readline, b""):
      if(line != b"\n"):
        if(len(line.split(b" ")) == 4):
          try:
            if(int(float(line.split(b" ")[2])) == value): 
              output_file.write(line)
          except ValueError:
            continue
    mmap_file.flush()
    
    f.close()
    output_file.close()



# THIRD ITERATION (20s +- 171ms/loop => 14% increase from 2nd It.)  
# Using Slicing Instead of Data Type Conversion 
# - Instead of using float then int, use slicing as string operations are faster than data conversions 
# - Line105: slicing the row to get 3rd element then converting the string to int to do comparison ("1 0 3098 3100.10 54188" => "3100.10" => 3100)
def Function4(file):
  output      = "result.txt"
  output_file = open(output, "wb")
  value = int(3100.10)

  with open(file, "r+b") as f:
    mmap_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    for line in iter(mmap_file.readline, b""):
      if(line != b"\n"):
        if(len(line.split(b" ")) == 4):
          try:
            if(int(line.split(b" ")[2][:-3]) == value):
              output_file.write(line)
          except ValueError:
            continue
    mmap_file.flush()
  f.close()
  output_file.close()

  
# FOURTH ITERATION (6.22s +- 55.8ms/loop => 221.5% increase from 3rd It.)
# Using the Find Operation
# https://docs.python.org/3/library/mmap.html
# - Before = iterating through lines, iterate through line, extract 3rd value, compare
# - Now = look (find) desired value in each line
def Function5(file):
  output      = "results.txt"
  output_file = open(output, "wb")
  value = int(3100.10)
  value = (str(value) + ".").encode()
  
  with open(file, "r+b") as f:
    mmap_file = mmap.mmap(f.fileno(), 0, acccess=mmap.ACCESS_READ)
    for line in iter(mmap_file.readline, b""):
      find = line.find(value)
      if (find >= 7 and find <= 11):
        output_file.write(line)
    mmap_file.flush()
  f.close()
  output_file.close()