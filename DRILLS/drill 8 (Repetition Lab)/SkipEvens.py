# Implement skip_evens(start, end). Return a list of odd numbers from 
# start to end inclusive. Use continue to skip even numbers.
# If start is greater than end, return an empty list.

def skip_evens(start, end):

    if start > end:
        return []
    
    odd_numbers = []

    for number in range(start,end+1):
        
        if number % 2 == 0:
            continue

        odd_numbers.append(number)


    return odd_numbers

print(skip_evens(1,10))
print(skip_evens(10,1))