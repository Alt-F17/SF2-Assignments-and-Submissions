import json

# making a dictionary
data = {"name":"John", "age": 30, "city": "New York"}

# converting dictionary to JSON
json_data = json.dumps(data)
print(type(json_data))
print(json_data)



# converting JSON to dictionary
data = json.loads(json_data)
print(type(data))
print(data)


# reading JSON from a file
with open(r"In Class Notes and Activities\Class Notes Code\students.json", "r") as input_file:
    data = json.load(input_file)
    print(type(data))
    print(data)


# writing JSON to a file
with open(r"In Class Notes and Activities\Class Notes Code\students.json", "w") as output_file:
    json.dump(data, output_file, indent=4)
    print(type(data))
    print(data)


# modifying JSON data
john_index = next((i for i, student in enumerate(data["students"]) if student["name"] == "John Doe"), -1)
data["students"][john_index]["age"] = 35 if john_index != -1 else None

# writing modified JSON to a file
with open(r"In Class Notes and Activities\Class Notes Code\students.json", "w") as output_file:
    json.dump(data, output_file, indent=4)
    print(type(data))
    print(data)


# Notes:

# - JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate.
# - JSON is language-independent, meaning it can be used with any programming language that supports JSON parsing and generation.

# .dump() is used to write JSON data to a file.
# .dumps() is used to convert a Python object to a JSON string.
# .load() is used to read JSON data from a file and convert it to a Python object.
# .loads() is used to convert a JSON string to a Python object.


# main difference between saving the input file in a variable VS using the with statement:
# - Using the with statement automatically closes the file after the block of code is executed, ensuring that resources are properly managed.
# - Saving the input file in a variable requires manual closing of the file, which can lead to resource leaks if not done properly.
# - Using the with statement is generally considered a best practice for file handling in Python.
# - The with statement also provides better readability and maintainability of the code.
# - The with statement is also more efficient, as it reduces the number of lines of code and makes it easier to handle exceptions.



# to seek to the 10th line of the file:
# use data.seek(0) to move the file pointer to the beginning of the file, and then use a loop to read each line until you reach the 10th line.
# can you read only lines 10 to the end?
# yes, you can use the readlines() method to read all lines into a list and then slice the list to get the desired lines.
# for example:
# with open("file.txt", "r") as file:
#     lines = file.readlines()
#     for line in lines[9:]:  # this will read lines 10 to the end
#         print(line.strip()) # what does strip() do? 
# strip() removes leading and trailing whitespace characters (including newlines) from the string.
# this will read lines 10 to the end