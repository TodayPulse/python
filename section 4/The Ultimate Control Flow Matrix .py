# Challenge 5: The Ultimate Control Flow Matrix (Combined Master Test)
# Concepts Tested: Combining everything: Functions, nested loops (for + while), lambda validation, break, 
# continue, and if-else.

# The Task: Write a function named matrix_cruncher(matrix, threshold_lambda) where matrix is a list of lists 
# containing integers.

# Iterate through each row and each element using nested loops.

# Pass each element through the threshold_lambda. If the lambda evaluates to False, skip that element using 
# continue.

# If the element is an exact match to a system-wide hazard code (0), terminate the entire row's processing
# immediately using a break statement.

# If an element makes it past both checks, add it to a running accumulator total.

# Return a dictionary summarizing the result: {"total": accumulator_sum, "status": "Secure"}.

def matrix_cruncher(matrix, threshold_lambda):

    accumulator = 0

    for row in matrix:

        index = 0

        while index < len(row):

            element = row[index]

            if element == 0:
                break

            if not threshold_lambda(element):
                index += 1
                continue

            accumulator += element
            index += 1

    
    return {"total": accumulator, "status": "Secure"}


# --- Example usage ---
matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [-1, 5, 8]
]

result = matrix_cruncher(matrix, lambda x: x > 0)
print(result)
