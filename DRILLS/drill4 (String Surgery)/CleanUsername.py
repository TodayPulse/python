# Implement clean_username(value). The function should remove leading
# and trailing spaces, convert the text to lowercase, and replace every 
# space with an underscore. Return the cleaned username.

def cleanUsername(value):
    value = value.strip()
    value = value.lower()
    value = value.replace(" ","_")

    return value

print(cleanUsername("Olowu Emmanuel"))
