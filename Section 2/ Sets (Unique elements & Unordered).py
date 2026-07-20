
# QUESTION 1
# Deduplication: 
# Write a function that takes a list with duplicate elements and 
# returns a list containing only unique 
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

# QUESTION 3
# Membership: 
# Check if all elements of a set subset are present in a set main_set 
# (hint: look for issubset).

main_set = {1, 2, 3, 4, 5, 6}
subset = {2, 4, 6}

# Method 1: Using the .issubset() method
is_subset = subset.issubset(main_set)

# Method 2: Using the <= operator
# This is a shorthand way to perform the same check
is_subset_alt = subset <= main_set

print(f"Is the subset part of the main set? {is_subset}")


# QUESTION 4
# Filtering: 
# Create a set of words from a string, then remove all words that start with the letter 'a' 
# (case-insensitive).

text = "Apple banana apricot cherry avocado date"

splited = set(text.split())

flitered_set = {word for word in splited if not word.lower().startswith('a')}

print(f"flitered word is : {flitered_set}")