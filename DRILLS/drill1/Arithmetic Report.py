# Write a function called `solution` that receives a student's name 
# and three numbers.

# Return a four-line report in this exact format:

# Student: <name>
# Sum: <sum>
# Average: <average>
# Maximum: <maximum>

# Rules:
# - Add the three numbers to get the sum.
# - Divide the sum by 3 to get the average.
# - Round the average to 2 decimal places.
# - Find the largest number.
# - Return the final multi-line string.
# - Do not print.

def solution(name, a, b, c):
    return f"Student: {name}\nSum: {a+b+c}\nAverage: {round((a+b+c)/3,2)}\nMaximum: {max(a,b,c)}"

print(solution("Olowu Emmanuel",10,20,30))

# Better fix
def solution(name, a, b, c):
    total = a + b + c
    average = round(total / 3, 2)
    maximum = max(a, b, c)
    return f"Student: {name}\nSum: {total}\nAverage: {average}\nMaximum: {maximum}"

print(solution("Olowu Emmanuel", 10, 20, 30))