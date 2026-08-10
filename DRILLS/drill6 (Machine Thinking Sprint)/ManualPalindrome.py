# Implement manual_palindrome(text). Ignore spaces and letter case. Return true if the cleaned text reads 
# the same forward and backward, otherwise return false. Do not use slicing shorthand or reversed. 
# Students may need to research manual string reversal.

def manual_palindrome(text):
    cleaned = text.replace(" ","").lower()

    result = ""
    for char in cleaned:
        result = char + result

    return cleaned == result


# Example usage
print(manual_palindrome("Never Odd Or Even"))  # True
print(manual_palindrome("Hello World"))        # False
