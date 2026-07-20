# QUESTION 1
# Arithmetic & Assignment Operators
# The Modulo & Floor Division Challenge: 
# Write a script where a user can input a total number of seconds (e.g., 9875). 
# Convert this into hours, minutes, and remaining seconds using only // and %.

total_seconds = (int(input("Enter the amount of seconds : ")))
hours = total_seconds // 3600

remaining_seconds = total_seconds % 3600;

minutes = remaining_seconds // 60;

seconds = remaining_seconds % 60;

print(f"{hours} hour(s) : {minutes} minutes : {seconds} seconds")

# QUESTION 2
# Compound Interest Calculator: Create variables for principal amount (P), 
# annual interest rate (r), time in years (t), and number of times interest 
# is compounded per year (n). Use the formula A = P(1 + r/n)^{nt} with the exponentiation operator () 
# to calculate the final amount.

principal = (int(input("Enter principal amount : ")))
Interest = (int(input("Enter interest rate : ")))
Time = (int(input("Enter time interval : ")))
Number = (int(input("Enter the number of times interest is computted in a year : ")))


Amount = principal * (1 + (Interest)/Number) ** (Number*Time) 

print(Amount);


# QUESTION 3
# Compound Assignment Sequences: Start with x = 10. 
# Apply compound assignment operators in sequence: add 5, multiply by 3, subtract 2, 
# floor divide by 4, and raise to the power of 2. Print x after each operation.

x = 10
x += 5
print(x)
x *= 3
print(x)
x -= 2
print(x)
x //= 4
print(x)
x **= 2
print(x)