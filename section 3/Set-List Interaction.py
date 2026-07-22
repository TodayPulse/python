# Set-List Interaction: 
# Write a script that takes a list of full names. 
# Extract all unique first names and store them in a list, then sort that list alphabetically.


def unqiue(names):

    getUniqueNames = { firstNames.split()[0] for firstNames in names}

    sortedNames = sorted(getUniqueNames)

    return sortedNames

names_list = ["John Smith", "Jane Doe", "John Adams", "Alice Johnson", "Jane Eyre", "Alice Smith"]

print(unqiue(names_list))