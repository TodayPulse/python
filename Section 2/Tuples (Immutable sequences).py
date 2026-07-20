# QUESTION 1
# Unpacking: 
# Given a tuple (name, age, city), unpack it into three 
# separate variables and print them formatted.

user_info = ("Emmanuel", 27, "Ado")

name,age,city = user_info

print(f"Name:{name}, Age:{age}, City:{city}")

# QUESTION 2
# Immutability: 
# Write code to demonstrate what happens when you 
# try to change an element in a tuple. Explain why it fails.

fruits = ("Apple", "Orange", "Pineapple")

try:
    fruits[1]="mango"
except TypeError as e:

 print(f"Error caught: {e}")


#  QUESTION 3
#  Conversion: 
#  Take a list of numbers, convert it to a tuple, 
#  and then find the maximum value using max().

numbers_list = [10, 45, 2, 89, 33]

tuplel_list = tuple(numbers_list)

maximum = max(tuplel_list)

print(f"The maximun value is {maximum}")


# QUESTION 4
# Swapping: 
# Use tuple unpacking to swap the values of two 
# variables a and b without using a temporary variable.

a = 5
b = 10

print(f"Before swap: a = {a}, b = {b}")

# Swap using tuple unpacking
a, b = b, a

print(f"After swap: a = {a}, b = {b}")


# QUESTION 5

# Counting: 
# Given a tuple with repeating elements, write a function that returns the count of a specific element without 
# using the built-in .count() method.


def countNumber(tuple_list, element):
   count=0

   for n in tuple_list:
      if n == element:
         count+=1
    
   return count


list1 = ("a","a","b","c","c","c","e","e")

print(countNumber(list1,"c"))