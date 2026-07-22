# QUESTION 4
# The Collatz Sequence Analyzer (While Loop, If-Else Shorthand, Functions)
# Concepts Tested: Mathematical sequence generation, while loops, nested conditionals, and function modularity.

# The Task: Write a function collatz_length(n) that calculates how many steps it takes for a positive integer 
# n to reach 1 using the Collatz conjecture rules:

# If n is even, the next value is n // 2.

# If n is odd, the next value is 3 * n + 1.

# Use a while loop that runs as long as n > 1.

# Use an if-else shorthand (or standard inline logic) to compute the next value of n.

# Track and return the total number of steps taken to reach 1.


def collatz_length(n):

    step = 0

    while n > 1:
       
       n = n // 2 if n % 2 == 0 else 3 * n + 1
       step += 1

    return step


print(collatz_length(9))


    