# Implement first_and_last(value). Return a dictionary with two keys:
#  "first" and "last". "first" should contain the first character of the
#  string. "last" should contain the last character of the string. 
#  If the string is empty, return {"first": "", "last": ""}.

def first_and_last(value):
    if len(value) == 0:
        return {"first": "", "last": ""}
    return {"first": value[0], "last": value[-1]}


print(first_and_last("Olowu Emmanuel"))