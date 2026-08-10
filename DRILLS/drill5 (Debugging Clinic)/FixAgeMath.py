# Implement next_age(age_text). The function receives age as text.
# Convert it to an integer and return the age next year. This fixes the 
# common bug where text is used like a number.


def next_age(age_text):
    age_text = int(age_text)

    return age_text + 1
