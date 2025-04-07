# Question 1
'''
Open your story file from class for reading.
(a) Print the story (only the story) for the user to read
(b) Count the total number of words in the story
(c) Count the frequency of each word in the story.  Then sort all the available words
    in the story according to their frequence from highest to lowest. Display the results.
(d) Sort the words with the same frequency in alphabetical order. Display the results.
'''

# Solution:

# part a

with open(r"In Class Notes and Activities\Labs\Lab10\story.txt", "r") as file:
    story = file.read()
    print(story)

# part b

word_count = len(story.split())
print(f"Total number of words in the story: {word_count}")

# part c

word_frequency = {}
for word in story.split():
    word = word.lower()
    word_frequency[word] = word_frequency.get(word, 0) + 1

def key_parse(word_freq):
    return word_freq[1]

word_list_by_frequency = sorted(word_frequency.items(), key=key_parse, reverse=True)
print("Word frequency from highest to lowest:")
print(word_list_by_frequency)

# part d

def freq_then_alpha(word_freq):
    return (-word_freq[1], word_freq[0])

word_list_by_frequency_and_alpha = sorted(word_frequency.items(), key=freq_then_alpha)
print("Words sorted by frequency (highest to lowest) and then alphabetically:")
print(word_list_by_frequency_and_alpha)

# Question 2
'''
Make two files: cats.txt and dogs.txt.  Store at least three names of cats in the first
file and three names of dogs in the second file.  Write a program that tries to read
these files and print the contents of each file to the screen.  

(a) Wrap your code in a try-except block to catch the FileNotFoundError and print a 
    friendly message if a file is missing.  To test your code, move one of the files 
    to a different location on your system, and make sure that the code in the except 
    block executes properly.  
(b) Modify your previous code to fail silently if either file is missing
'''

# Solution:
try: 
    with open("cats.txt", "r") as cats_file:
        cats = cats_file.read()
        print("Cats:")
        print(cats)

except FileNotFoundError as e:
    print(f"File not found: {e.filename}")

# Question 3
'''
A common problem when prompting for numerical input occurs when providing text 
instead of numbers.  In such a case, when trying to convert the input to int, a
ValueError occurs.  Write a program that prompts the user for two numbers, add
them together and print the result.  Catch the ValueError if either input value is
not a number, and print a friendly error message.  Test your program by entering two
numbers and then by entering some text instead of a number.  
'''

# Solution:
def add_numbers():
    while 1:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            return f"The sum of {num1} and {num2} is: {num1 + num2}"
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

print(add_numbers())