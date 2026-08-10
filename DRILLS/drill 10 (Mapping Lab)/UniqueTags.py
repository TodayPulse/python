# Implement unique_tags(tags). Clean each tag by stripping spaces
# and converting to lowercase. Ignore empty tags. 
# Return a sorted list of unique cleaned tags.

def unique_tags(tags):

    unique_tags = []

    for tag in tags:
        tag = tag.strip().lower()

        if not tag:
            continue

        if tag in unique_tags:
            continue

        elif tag not in unique_tags:
            unique_tags.append(tag)

        unique_tags.sort()

    return unique_tags

print(unique_tags(["Python","python"," AI ","ai"]))
