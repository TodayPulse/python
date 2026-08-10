# Implement dedupe_preserve_order(items). 
# Return a new list with duplicate values removed while keeping the 
# first time each value appeared. 
# Do not use set for this challenge.

def dedupe_preserve_order(items):

    new_list = []

    for item in items:
        if item not in new_list:
            new_list.append(item)

    return new_list

print(dedupe_preserve_order([1,2,1,3,2]))