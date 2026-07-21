# Nested Data Extraction: 
# Given a dictionary where values are lists of tuples
# (e.g., {'ClassA': [('John', 85), ('Jane', 92)]}),
#  write a function to return a list of all names regardless of the class.



def extract_all_names(data_dict):
    """
    Extracts and returns a flat list of all names from a dictionary 
    where values are lists of (name, score) tuples.
    """
    all_names = []
    
    # Iterate through each class list in the dictionary values
    for student_list in data_dict.values():
        # Each student_list contains tuples of (name, score)
        for score, s in student_list:
            all_names.append(score)
            
    return all_names

# --- Example Usage ---
school_data = {
    'ClassA': [('John', 85), ('Jane', 92)],
    'ClassB': [('Bob', 78), ('Alice', 95), ('Charlie', 88)]
}

print(extract_all_names(school_data)) 
Output: ['John', 'Jane', 'Bob', 'Alice', 'Charlie']