# Importation
import matplotlib.pyplot as plt
from pynput import keyboard

# Input number
input_number = int(input('What number would you like to calculate? '))
current_number = input_number

# Variables
calculating = True
calculated_numbers = []
numbers_amount = []
number_count = 0
questioning = True
question_counter = 0
answer_list = ['YES', 'Yes', 'yes', 'JA', 'Ja', 'ja', 'JEP', 'JIP', 'Jep', 'Jip', 'jep', 'jip']
question_answer = None

# Questioning loop
while questioning:
# Calculation loop
    while calculating:
        
        # Calculation
        if (current_number % 2) == 0:
            current_number /= 2
        else:
            current_number *= 3
            current_number += 1

        # Number counting
        number_count += 1
        numbers_amount.append(number_count)

        # Showing numbers
        print(str(int(current_number)))
        
        # Appending to calculated numbers
        if current_number not in calculated_numbers:
            calculated_numbers.append(int(current_number))

        # Ending calculations if 1
        if current_number == 1:
            print('Here are all the numbers we have calculated' , str(sorted(calculated_numbers)))
            calculating = False

    # Graph creation
    fig, ax = plt.subplots()
    ax.plot(numbers_amount, calculated_numbers)
    plt.show()

    # Asking for further calculations
    question_answer = input('Do you want to calculate another number? ')

    # Checking answer 
    if question_answer in answer_list:
        # Resetting calculations
        calculating = True
        calculated_numbers = []
        numbers_amount = []

        # Setting new current number
        current_number = int(input('What is the next number you want to calculate? '))
    else:
        questioning = False
