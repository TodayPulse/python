# Implement chunk_list(items, size). Split items into smaller lists of length 
# size. 
# The final chunk may be shorter if there are not enough items left. 
# If size is less than 1, return Invalid size.

def chunk_list(items, size):

    if size < 1:
        return "Invalid size"

    chunk = []

    for skip_count in range(0,len(items),size):
        chunk.append(items[skip_count:skip_count+size])

    return chunk

print(chunk_list([1,2,3,4,5],2))


    