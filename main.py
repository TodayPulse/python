def exact_calculator(left, operator, right):

    def to_number(value):
        try:
            return int(value)
        except(ValueError, TypeError):
            pass
        try:
            return float(value)
        except(ValueError, TypeError):
            return None

    left_num = to_number(left)
    right_num = to_number(right)

    if left_num is None or right_num is None:
        return "Invalid number"

    valid_operators = ["+", "-", "*","/","%","**"]
    if operator not in valid_operators:
        return "Invalid operator"

    if operator in ("/", "%") and right_num == 0:
        return "Cannot divide by zero"

    if operator == "+":
        result = left_num + right_num
    elif operator == "-":
        result = left_num - right_num
    elif operator == "*":
        result = left_num - right_num
    elif operator == "/":
        result = left_num / right_num
    elif operator == "%":
        result = left_num % right_num
    elif operator == "**":
        result = left_num ** right_num

    
