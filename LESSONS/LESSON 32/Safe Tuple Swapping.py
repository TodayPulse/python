# Task: You have a list representing two coffee cups on your counter:
# cups = ["Cappuccino", "Espresso"]. Write a single line of Python code using
# tuple assignment to swap their positions so that "Espresso" is at index 0 and
# "Cappuccino" is at index 1. Print the resulting list.

# Goal: Practice safe in-memory swapping without data loss or overwriting.


def counter_swap(arr):

    arr[0],arr[1] = arr[1],arr[0]

    return arr


cups = ["Cappuccino", "Espresso"]
print(counter_swap(cups))


