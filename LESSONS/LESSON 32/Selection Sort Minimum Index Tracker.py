# Selection Sort Minimum Index Tracker

# Task: Write a Selection Sort function named selection_sort_prices(arr). 
# Ensure that your code tracks the index of the minimum element (min_index) 
# during the inner loop scan rather than tracking the value itself, swapping it safely at the end of
# each outer loop iteration.

# Goal: Master the distinct logic of Selection Sort (scanning for minimum indices before swapping).


def selection_sort_prices(arr):
    length = len(arr)

    for i in range(length):
        min_index = i

        for j in range(i+1,length):

            if arr[j] < arr[min_index]:
                min_index = j

        arr[i] , arr[min_index] = arr[min_index], arr[i]

prices = [6.00, 1.50, 4.00, 3.00, 5.50]
selection_sort_prices(prices)
print(prices)



