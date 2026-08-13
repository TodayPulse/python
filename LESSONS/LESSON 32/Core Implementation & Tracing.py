# Complete Bubble Sort Implementation
# Task: Write a complete Python function named bubble_sort_cups(arr) 
# that accepts a list of numerical coffee prices and sorts them in 
# ascending order using the Bubble Sort algorithm. Test your function with prices =
#  [6.00, 1.50, 4.00, 3.00, 5.50] and print the sorted output.

# Goal: Implement nested loops and adjacent condition swaps correctly from scratch.


def bubble_sort_cups(arr):

    length = len(arr)

    for count in range(length):
        for i in range(0, length-count - 1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1], arr[i]

    return arr

prices = [6.00, 1.50, 4.00, 3.00, 5.50] 
print(bubble_sort_cups(prices))