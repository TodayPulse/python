# Implement slug_maker(title). Remove leading and trailing spaces, convert the text to lowercase, 
# remove commas and periods, and replace spaces with hyphens. Return the final slug.

def slug_maker(title):
    title = title.strip().lower()
    title = title.replace(",","").replace(".","")
    title = title.replace(" ","-")

    return title

print(slug_maker("  Hello, World. This is a Test.  "))

