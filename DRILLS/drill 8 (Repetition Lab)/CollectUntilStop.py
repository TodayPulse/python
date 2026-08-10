# Implement collect_until_stop(items). Loop through the list and collect
# items until an item becomes stop after stripping spaces and converting 
# to lowercase. Return the collected items before stop.
# Use break when stop is found.

def collect_until_stop(items):

    store = []
    for item in items:
        item = item.strip().lower()

        if item == "stop":
            break
        else:
            store.append(item)

    return store

print(collect_until_stop(["red","blue","stop","green"]))