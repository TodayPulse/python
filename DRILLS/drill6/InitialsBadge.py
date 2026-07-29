# Implement initials_badge(full_name). Remove leading and trailing spaces, split the name into words, 
# take the first character of each word, convert each initial to uppercase, and return the initials joined with
# dots. The returned badge should end with a dot.

def initials_badge(full_name):
    full_name = full_name.strip()

    words = full_name.split()

    initials = (word[0].upper() for word in words)

    badge = ".".join(initials) + "."


    return badge


# Example usage
print(initials_badge("  emmanuel john doe  "))  # E.J.D.
print(initials_badge("madonna"))                 # M.
print(initials_badge("mary  jane   watson")) 