# Chained Comparisons: Given three variables x = 12, y = 18, and z = 15, 
# write a single chained comparison expression that checks if x is less than z and z is less than y. 
# Verify if it evaluates to True.

x =12
y=18
z=15
print(x<z<y)

# QUESTION 2
# String vs. Numeric Comparison: Write a script that compares the integer 5 
# with the float 5.0 using ==, and then compares the string "5" with the integer 5. 
# Observe and document the boolean outcomes.

print(5==5.0)
print("5"==5)

# QUESTION 3
# Lexicographical Comparison: Create two string variables with different words (e.g., "apple" and "banana"). 
# Write expressions to test which one is "greater" than the other using relational operators, 
# and verify how Python evaluates alphabetical ordering.

first = 'apple'
second = 'banana'

print(first > second)