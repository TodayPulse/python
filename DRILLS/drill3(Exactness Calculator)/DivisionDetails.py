# Implement division_details(a, b). Return a dictionary with three keys: 
# "true_division", "floor_division", and "remainder". true_division should 
# be a / b rounded to 2 decimal places. floor_division should be a // b. 
# remainder should be a % b.

def division_details(a, b):
    return{
        "remainder":a%b,
        "true_division":a/b,
        "floor_division":a//b
    }

print(division_details(10,3))
print(division_details(20,5))
