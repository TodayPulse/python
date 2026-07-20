# QUESTION 1

# Filtering: 
# Write a function that takes a list of integers and returns 
# a new list containing only the even numbers.

# Method 1: Using List Comprehension (Recommended)
def get_even_numbers(numbers):
    return [n for n in numbers if n%2 == 0]

my_list = [1,2,3,4,5,6,7,8,9,10]
print(get_even_numbers(my_list))
    

# Method 2: Using a For-Loop (Standard Approach)

def even_numbers(numbers):
    even_list = []

    for n in numbers:
        if n%2 == 0:
            even_list.append(n)
    return even_list

list2 = [11,12,13,14,15,16,17,18,19,20,21,22,23]

print(even_numbers(list2))




# QUESTION 2
# List Comprehension: 
# Use a list comprehension to create a 
# list of the squares of numbers from 1 to 10.
 
def create_square(numbers):
    return [n**2 for n in numbers]

list1 = [1,2,3,4,5,6,7,8,9,10]
print(create_square(list1))


#QUESTION 3
# Manipulation: 
# Given a list of strings, 
# write code to remove the second element, 
# append "Python" to the end, and reverse the entire list.

list3 = ["apple", "orange", "java", "css"]
del list3[1]  #or list3.remove("orange")
list3.append("Python")
list3.reverse()
print(list3)


# QUESTION 4
# Flattening: 
# Write a function that takes a list of lists 
# (e.g., [[1, 2], [3, 4]]) and returns a single flat list ([1, 2, 3, 4]).

def join_lists(nestedList):
    sublist = []
    for n in nestedList:
        sublist.extend(n)

    return sublist

list4 = [[1, 2], [3, 4]]
print(join_lists(list4))


def join_list(nestedList):
    return[n for subList in nestedList for n in subList]

list5 = [[1, 2,40,5], [3, 4,43]]
print(join_list(list5))


# QUESTION 5
# Searching: 
# Write a function that returns the index of the first 
# occurrence of a target number in a list; if the number is not found, return -1.

def index_pointer(list,number):

    for n in list:
        if n == number:
            return n
        
    return -1

list6=[1,2,3,4,5,6,7,8,9,10]
print(index_pointer(list6,10))






def find_number(lst, target):
    # This creates a list of all instances of 'target' found in the list
    return[n for n in lst if n == target else -1]
    
    # Return the target if the results list is not empty, otherwise return -1
    # return results[0] if results else -1


print(find_number(list6, 2))  # Output: 2
print(find_number(list6, 11)) # Output: -1

