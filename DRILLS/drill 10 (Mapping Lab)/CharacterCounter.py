# Implement character_counter(text).
# Return a dictionary where each character maps to how many
# times it appears. Count spaces and symbols too. 
# Do not use collections.Counter.

def character_counter(text):

    count ={}

    for char in text:
        count[char] = count.get(char,0) + 1

    return count

# Test cases
print(character_counter("hello world"))
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

print(character_counter("a-a!"))
# Output: {'a': 2, '-': 1, '!': 1}

print(character_counter(""))
# Output: {}