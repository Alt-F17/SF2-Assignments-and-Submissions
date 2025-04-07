import datetime
import random
devices = ["phone", "tablet", "laptop", "desktop", "smartwatch", "sandwich", 
           "smartfridge", "smarttoaster", "smarttoilet", "smartshoes"]
# Read phonebook.txt where each line has name and number
phonebook = {}
with open("phonebook.txt", "r") as file:
    names = []
    numbers = []
    for line in file:
        parts = line.strip().split()
        names.append(parts[0])
        numbers.append(parts[1])
        phonebook[parts[0]] = parts[1]
            
for i in range(40):
    with open("PhoneLog.txt", "a") as log_file:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_file.write(f"{now}: {random.choice(names)} called me on my {random.choice(devices)} at 514-{random.choice(numbers)}\n")

# open("<FILENAME>", "<MODE>") is used to open a file
# open().seek(0) is used to move the cursor to the beginning of the file
#       .read() is used to read the entire file
#       .splitlines() is used to split the file into lines
#       .strip() is used to remove leading and trailing whitespace
#       .readline() is used to read a single line
#       .readlines() is used to read all lines into a list
#       .write() is used to write to a file
#       .writelines() is used to write a list of lines to a file
#       .close() is used to close the file
#       .rstrip() is used to remove trailing whitespace
#       .lstrip() is used to remove leading whitespace