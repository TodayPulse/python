
# Digit Extraction: Given a 4-digit integer (e.g., x = 4567), 
# write expressions using arithmetic operators (// and %) to extract each digit individually 
# (thousands, hundreds, tens, and units) into separate variables. Then print them out.

# Hint: Think about how dividing by 10, 100, or 1000 can strip away or isolate digits. Give it a try!

x = 4567

# Thousands: Drop the last 3 digits
thousands = x // 1000  # 4

# Hundreds: Drop the last 2 digits (45), then grab the last digit
hundreds = (x // 100) % 10  # 45 % 10 -> 5

# Tens: Drop the last digit (456), then grab the last digit
tens = (x // 10) % 10  # 456 % 10 -> 6

# Units: Just grab the very last digit directly
units = x % 10  # 7

print(f"Thousands: {thousands}")
print(f"Hundreds: {hundreds}")
print(f"Tens: {tens}")
print(f"Units: {units}")