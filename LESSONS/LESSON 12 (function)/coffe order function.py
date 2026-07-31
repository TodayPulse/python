# Task 1 — Coffee Order Function
# Create a function named brew_coffee() that prints:

# Grinding espresso beans...
# Brewing coffee...
# Coffee is ready!
# Then call the function three times.

# Expected Output:

# Grinding espresso beans...
# Brewing coffee...
# Coffee is ready!

# Grinding espresso beans...
# Brewing coffee...
# Coffee is ready!

# Grinding espresso beans...
# Brewing coffee...
# Coffee is ready!

def brew_coffee():
    answer = "Grinding espresso beans...\nBrewing coffee..\nCoffe is ready!\n"

    count = 0

    while count <= 2:
        print(answer)
        count += 1


brew_coffee()