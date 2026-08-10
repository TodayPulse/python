# Implement deep_flatten(items). Return a flat list containing every 
# non-list value from items, no matter how deeply nested the lists are. 
# Students may need to research recursion. Preserve the left-to-right
# order.

def deep_flatten(items):

    result = []

    for item in items:
        if isinstance(item, list):
            result.extend(deep_flatten(item))

        else:
            result.append(item)

    return result

print(deep_flatten([1,[2,3],4]))
        
    