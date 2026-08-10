# Implement exact_calculator(left, operator, right). Convert left and right to numbers.
# Support addition, subtraction, multiplication, division, remainder, and exponent. 
# If either number cannot be converted, return Invalid number. If the operator is not supported,
# return Invalid operator. If division or remainder uses zero on the right side, return Cannot divide by zero.
# Round numeric results to 2 decimal places.

def exact_calculator(left, operator, right):
    # Try to convert both sides to numbers
    def to_number(value):
        try:
            return int(value)
        except (ValueError, TypeError):
            pass
        try:
            return float(value)
        except (ValueError, TypeError):
            return None

    left_num = to_number(left)
    right_num = to_number(right)

    if left_num is None or right_num is None:
        return "Invalid number"

    valid_operators = ["+", "-", "*", "/", "%", "**"]
    if operator not in valid_operators:
        return "Invalid operator"

    if operator in ("/", "%") and right_num == 0:
        return "Cannot divide by zero"

    if operator == "+":
        result = left_num + right_num
    elif operator == "-":
        result = left_num - right_num
    elif operator == "*":
        result = left_num * right_num
    elif operator == "/":
        result = left_num / right_num
    elif operator == "%":
        result = left_num % right_num
    elif operator == "**":
        result = left_num ** right_num

    return round(result, 2)


# Example usage
print(exact_calculator("10", "+", "5"))     # 15
print(exact_calculator("10", "/", "3"))     # 3.33
print(exact_calculator("10", "/", "0"))     # Cannot divide by zero
print(exact_calculator("abc", "+", "5"))    # Invalid number
print(exact_calculator("10", "^", "2"))     # Invalid operator
print(exact_calculator("2", "**", "8"))     # 256