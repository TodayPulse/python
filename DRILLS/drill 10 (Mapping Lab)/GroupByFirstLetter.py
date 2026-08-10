# Implement group_by_first_letter(names). Return a dictionary
# where each key is the uppercase first letter of a name and 
# each value is a list of names that start with that letter.
#  Ignore empty names after stripping spaces.
#  Preserve the order of names inside each group.

def group_by_first_letter(names):

    result = {}

    for name in names:
        word = name.strip()

        if not word:
            continue

        first_letter = word[0].upper()

        if first_letter not in result:
            result[first_letter] = []


        result[first_letter].append(word)

    return result

print(group_by_first_letter(["Ada","Halima","Adamu","Tunde"])) 


