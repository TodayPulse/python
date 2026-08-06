# Implement safe_calculator(a, operator, b). Return the result of applying 
# the operator to the two numbers. Supported operators are 
# "+", "-", "*", "/", "%", and "**". If the operator is unknown, return
# "Invalid operator". If the operator is "/" or "%" and b is 0, return 
# "Cannot divide by zero". Round division results to 2 decimal places.

def safe_calculator(a, operator, b):
    valid_operator = ["+","-","*","/","%","**"]

    if operator not in valid_operator:
        return "Invalid operator"

    if (operator == "/" or operator == "%") and b == 0:
        return "Cannot divide by zero"

    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        return round(a/b,2)
    elif operator == "%":
        return a%b
    elif operator == "**":
        return a**b


print(safe_calculator(5,"+",3))
print(safe_calculator(10,"-",4))
print(safe_calculator(10,"/",4))


    
  


    