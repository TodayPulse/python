# Implement safe_divide(a, b). 
# Return a divided by b rounded to 2 decimal places. 
# If b is zero, return Cannot divide by zero. 
# This fixes the common ZeroDivisionError bug.

def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return round(a/b,2)

