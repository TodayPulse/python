# QUESTION

# Short-Circuit Evaluation Exploration: 
# Create a function that prints a message 
# and returns False. Use it alongside a standard False boolean in an and statement, 
# and a True boolean in an or statement to see if Python evaluates the second operand (short-circuiting).


def check_condition():
    print("Function Executed!")
    return False

print("Here is the first shot...")

result1 = False and check_condition()

print("Here is the second shot ...")
result2 = True or check_condition()

print("Here is the third shot..")
result3 = False or check_condition()


# QUESTION 2
# Leap Year Logic: 
# A year is a leap year if it is divisible by 4, 
# but not by 100 unless it is also divisible by 400. Write a single logical statement using and, or, 
# and not to determine if a variable year is a leap year.

year = 2020  # Change this to test different years

is_leap_year = (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0)

print(f"is {year} a leap year?  {is_leap_year}")


# QUESTION 3
# Membership Assessment: Create a list of restricted usernames. 
# Write a script that takes an input username and uses logical operators combined 
# with membership operators (in / not in) to check if the username is available and valid 
# (e.g., length greater than 5).

# 1. Create a list of restricted usernames
restricted_usernames = ["admin", "root", "superuser", "moderator"]

# 2. Get input from the user
name = input("Enter Username: ")

# 3. Check both conditions using membership and logical operators
# Condition 1: Must NOT be in the restricted list
# Condition 2: Length must be greater than 5
is_valid_and_available = (name not in restricted_usernames) and (len(name) > 5)

# 4. Print the result
print(f"Is '{name}' available and valid? {is_valid_and_available}")