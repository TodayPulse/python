# Nested Data Extraction: 
# Given a dictionary where values are lists of tuples 
# (e.g., {'ClassA': [('John', 85), ('Jane', 92)]}),
#  write a function to return a list of all names regardless of the class.


def extract(dict_list):

    all_names = []

    for student_list in dict_list.values():

        for name, score in student_list:
            all_names.append(name)
            
    return all_names

school_data = {
    'ClassA': [('John', 85), ('Jane', 92)],
    'ClassB': [('Bob', 78), ('Alice', 95), ('Charlie', 88)]
}

print(extract(school_data)) 
# Output: ['John', 'Jane', 'Bob', 'Alice', 'Charlie']