# Question 1
'''
From your accounts.txt file (from last class) read each line and create 
a dictionary of dictionaries.  The outer dictionary key is the account 
number.  The inner dictionary key is the last name and the value in 
the inner dictionary is the balance.  Print the final dictionary.  
'''

accounts = {}
for line in open(r'C:\Users\felix\OneDrive - Dawson College\Class Files\SF2 - Coding\SF2-Assignments-and-Submissions\In Class Notes and Activities\Labs\lab9\accounts.txt'):
    account_number, last_name, balance = line.strip().split()
    accounts[account_number] = {last_name: balance}

print(accounts)

# Question 2
'''
(a) Open a file called grades.txt for writing that will hold student 
    grade information.  This information will be read from the user.  
    Each input line given by the user is of the form: 
    firstname, lastname, exam1grade, exam2grade, exam3grade.  
    Read grade information for 10 students and write that information 
    to your grades.txt file.  Make sure to close the file after 
    writing to it.  

(b) Once your grades.txt file is populated, read and store the infomration
    from the file.  Determine what data structure (e.g. lists, dictionaries, 
    sets, etc.) would best suit for storing the data in the file.  Once 
    your data is stored, compute the following: 
    (i) the minimum, maximum and average of exam1grade, exam2grade, exame3grade
        for each student and print this information
    (ii) the minimum, maximum and average of exam1grade across all students.
         Do this for exam2grade and exam3grade as well.  
    (iii) the average of the average of all 3 exams for all students.  
'''

# Part a
grades = open('grades.txt', 'w')
for _ in range(10):
    grades.write(input() + '\n')
grades.close()

# Part b
grades = open('grades.txt', 'r')
students = []
for line in grades:
    first_name, last_name, exam1, exam2, exam3 = line.strip().split(',')
    students.append({'first_name': first_name, 'last_name': last_name, 'exam1': int(exam1), 'exam2': int(exam2), 'exam3': int(exam3)})
grades.close()

for student in students:
    print(f"{student['first_name']} {student['last_name']}:")
    print(f"Exam 1: {student['exam1']}")
    print(f"Exam 2: {student['exam2']}")
    print(f"Exam 3: {student['exam3']}")
    print()

exam1_grades = [student['exam1'] for student in students]
exam2_grades = [student['exam2'] for student in students]
exam3_grades = [student['exam3'] for student in students]

for i, grades in enumerate([exam1_grades, exam2_grades, exam3_grades], 1):
    print(f"Exam {i} Min: {min(grades)}")
    print(f"Exam {i} Max: {max(grades)}")
    print(f"Exam {i} Avg: {sum(grades) / len(grades)}")
    print()
