# Implement count_up(n). Return a list of numbers from 1 to n inclusive.
# If n is less than 1, return an empty list.
# Use a loop and range.


def count_up(n):
    
    result = []


    for number in range(1,n+1):
        result.append(number)

    return result

print(count_up(5))
print(count_up(0))
