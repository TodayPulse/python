
# QUESTION 1
# Deduplication: 
# Write a function that takes a list with duplicate elements and returns a list containing only unique 
# elements using sets.

def deduplication(item):
    return list(set(item))

my_list = [1, 2, 2, 3, 4, 4, 5, "a", "a", "b"]

print(deduplication(my_list))


# QUESTION 2
# Set Math: 
# Given two sets A = {1, 2, 3, 4} and B = {3, 4, 5, 6}, 
# find the union, intersection, and difference (A - B).

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union: All unique elements from both sets
union_set = A | B  # or A.union(B)

# Intersection: Elements present in both sets
intersection_set = A & B  # or A.intersection(B)

# Difference: Elements in A that are NOT in B
difference_set = A - B  # or A.difference(B)

print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Difference (A - B): {difference_set}")