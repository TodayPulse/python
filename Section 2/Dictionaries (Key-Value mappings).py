# QUESTION 1

# Frequency Counter: 
# Write a function that counts the frequency of every word in a
# string and stores it in a dictionary.

def count_word_frequency(text):
    # Split the text into a list of words
    words = text.split()
    
    # Initialize an empty dictionary
    frequency = {}
    
    for word in words:
        # Normalize to lowercase so 'Apple' and 'apple' are counted together
        word = word.lower()
        
        # If the word is already in the dict, increment; 
        # otherwise, add it with a count of 1
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
            
    return frequency

# Example usage:
text_input = "Apple banana apple cherry banana apple"
result = count_word_frequency(text_input)

print(result)
# Output: {'apple': 3, 'banana': 2, 'cherry': 1}

# QUESTION 2
# Merging: 
# Given two dictionaries, merge them into a third dictionary. 
# If a key exists in both, sum their values.

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 10, 'd': 40}

merged = dict1.copy()

for key, value in dict2.items():
    
    if key in merged:
        merged[key] += value
    else :
        merged[key] = value  

print(merged)


# QUESTION 3
# Transformation: 
# Given a dictionary of names and scores, return a new dictionary where only people 
# with scores above 80 are included.

scores = {"Alice": 92, "Bob": 75, "Charlie": 88, "David": 60}

high_scores = {}

for name, score in scores.items():
    if score > 80:
        high_scores[name] = score

print(high_scores)


# QUESTION 4
# Inversion: 
# Write code to invert a dictionary (keys become values, values become keys). 
# Assume all values are unique.


straight = {"Alice": 92, "Bob": 75, "Charlie": 88, "David": 60}

invert = {}

for key, name in straight.items():
    invert[name]=key

print(invert)    
