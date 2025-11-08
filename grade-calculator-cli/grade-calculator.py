"""
    
    Developer: Kerem Can Belli
    Project: Python Starter Algorithms and CLI Applications
    Subproject: Grade Calculator
    Description: Updated English version with structured comments
    Last Review: November 2025

"""

##########################################################################

# Fundamental variables are identified
grade_counter = 1
grade_list = []

##########################################################################

"""

    Project's main menu:

    * It is questioned how many grades users enter.
    * Input is validated using try-except blocks to handle non-integer input.
    * It is checked that grades which users enter are between 0 - 100.

"""

print("\n--- GRADE CALCULATOR ---")
while True:
    try:
        grade_amount_input = (input("Enter the number of grades to calculate: "))
        grade_amount = int(grade_amount_input) # grade_amount_input is converted to integer.
        if grade_amount < 0: # it is checked that grade_amount is bigger than 0.
            print("ERROR: Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("ERROR: Please enter an integer.")
while grade_counter<=grade_amount:
    try:
        grades_input = (input(f"Enter the {grade_counter}. grade: "))
        grades = int(grades_input)
        if grades < 0 or grades > 100: # it is checked grades are between 0 - 100.
            print("ERROR: Please enter an integer between 0 - 100.")
            continue
        grade_list.append(grades) # grades are appended in grade_list
        grade_counter += 1
    except ValueError:
        print("ERROR: Please enter an integer.")
        

# grades are summed and their average is taken.

sum_of_grades = sum(grade_list)
average = sum_of_grades/grade_amount

##########################################################################

"""

    Letter Grade Section:

    * Letter Grade is determined depends on average

"""

if average>=90:
    letter_grade = "AA"
elif average>=80:
    letter_grade = "BA"
elif average>=70:
    letter_grade = "BB"
elif average>=60:
    letter_grade = "CC"
elif average>=50:
    letter_grade = "DC"
else:
    letter_grade = "FF"

##########################################################################

"""

    Output section:

    * Grades, average and letter grade are showed

"""

print("\n--- RESULTS ---")
print(f"Grades that you entered: {grade_list}")
print(f"Your average: {average:.2f}")
print(f"Your letter grade: {letter_grade}")