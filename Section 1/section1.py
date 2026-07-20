# Swap Without Temporary Variable: Create two variables a = 5 and b = 10. 
# Swap their values without using a third temporary variable or arithmetic operators 
# (hint: use tuple unpacking)

a = 5;
b = 10;

a, b = b, a

print(f"a:{a}, b:{b}")

# Type Mutation Tracker: Assign the value "100" to a variable. 
# Print its type. Convert it to an integer, multiply it by 2, 
# and print the new value and type. Finally, convert it to a float and divide it by 4, 
# printing the final value and type.

# 1. Assign "100" and print its type
number = "100"
print(type(number))  # Output: <class 'str'>

# 2. Convert to integer, multiply by 2, print new value and type
number = int(number) * 2
print(number)        # Output: 200
print(type(number))  # Output: <class 'int'>

# 3. Convert to float, divide by 4, print final value and type
number = float(number) / 4
print(number)        
print(type(number))  


# Dynamic Reassignment Challenge: Create a variable named data. 
# Assign it an integer, then a string, then a list, and finally a dictionary. 
# Print the type of data after each assignment to observe Python’s dynamic typing in action.

data = 200
print(type(data))

data = "Hello World"
print(type(data))

data = ["apple","Orange"]
print(type(data))

data = {"name" : "Alice", "age":25}
print(type(data))



