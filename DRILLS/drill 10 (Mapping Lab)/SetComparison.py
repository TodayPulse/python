# Implement set_comparison(a, b). Return a dictionary with keys 
# named both, only_a, and only_b. The both value should be a 
# sorted list of items in both lists. The only_a value should be 
# a sorted list of items only in a. 
# The only_b value should be a sorted list of items only in b.

def set_comparison(a, b):
    a = set(a)
    b = set(b)

    return {
        "both": sorted(list(a & b)),
        "only_a": sorted(list(a - b)),
        "only_b": sorted(list(b - a)),
    }

print(set_comparison([1,2,3],[2,3,4]))