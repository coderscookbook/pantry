# https://medium.com/@hafizabdullaha93/20-extremely-useful-single-line-python-codes-de44928a1a3b

# 1. For Loops
my_list = [100, 200, 300, 40]
result = []
for x in my_list:
  if x > 150:
    result.append(x)
print(result)
# ONE LINE
result = [x for x in my_list if x > 250]
print(result)

# 2. While Loops
# 3. If Else Statment
# 4. Merging Dictionaries
# 5. Functions
# 6. Recursion
# 7. Filtering an Array
# 8. Exception Handling
# 9. Converting a List to a Dictionary
# 10. Multiple Variables
# 11. Swapping Values
# 12. Sorting
# 13. Reading a File
# 14. Class
# 15. Using Semicolon for Multiple Lines
# 16. Printing
# 17. Mapping
# 18. Deleting the Mul Elements from the First Row of a List
# 19. Print Pattern
# 20. Find Primes in a Range

######################################################################################
# RANDOM ONE LINERS
######################################################################################

# 1. Share WIFI password by printing as QR code
import wifi_qrcode_generator as qr
qr.wifi_qrcode('wifi name ', False, 'WPA', 'password')

# 2. CSV to JSON
import csv, json
print(json.dumps(list(csv.reader(open('csv_file.csv')))))

# 3. Apply regular expression to lines from stdin
import sys, re
[sys.stdout.write(re.sub('PATTERN', 'SUBSTITUTION', line)) for line in sys.stdin]

# 4. Display list of all users on unix-like systems
print '\n'.join(line.split(":", 1)[0] for line in open("/etc/passwd"))

# 5. Retrieve content text from HTTP data
print sys.stdin.read().replace('\r','').split('\n\n',2)[1]
