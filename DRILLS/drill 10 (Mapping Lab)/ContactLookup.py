# Implement contact_lookup(contact, key). The contact argument is a 
# dictionary. Return the value for the given key. If the key does not exist, 
# return Not found.


def contact_lookup(contact, key):

    return contact.get(key,"Not found")



print(contact_lookup({"age":22,"city":"Lagos","name":"Ada"},"name"))

def contact_lookup(contact, key):

    if key in contact:
        return contact[key]
    else:
        return "Not found"

