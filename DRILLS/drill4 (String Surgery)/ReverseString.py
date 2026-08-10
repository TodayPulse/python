# Implement reverse_string(value) without using slicing shorthand like [::-1].
# Return a new string containing the input characters in reverse order.

def reverse_string(value):

    result = ""
    for letters in value:
        result = letters + result

    return result

print(reverse_string("Emmanuel"))

