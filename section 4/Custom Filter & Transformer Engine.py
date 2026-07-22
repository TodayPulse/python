# QUESTION 2
# Challenge 2: Custom Filter & Transformer Engine (Functions, Lambda, Loops, continue)
# Concepts Tested: Functions taking functions (or lambda expressions), for loops, and the continue statement.

# The Task: Write a function named process_numbers(numbers_list, criteria_lambda) that:

# Iterates through a given list of integers using a for loop.

# Uses the provided criteria_lambda (a lambda function passed as an argument) to check a condition on each number.

# If the lambda returns False for a number, use the continue statement to skip it entirely.

# For numbers that pass, multiply them by 2 and append them to a new result list.

# Return the final modified list.

# Test case requirement: Pass a lambda function that checks if a number is odd (lambda x: x % 2 != 0).


def process_numbers(numbers_list, criteria_lambda):

    modifiedList = []

    for number in numbers_list:

        if not criteria_lambda(number):
            continue

        modifiedList.append(number * 2)

    return modifiedList


numberList = [0,1,2,3,4,5,6,7,8,9,10]
print(process_numbers(numberList, lambda x: x%2 != 0 ))

