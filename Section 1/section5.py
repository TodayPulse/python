# Identity vs. Equality: Create two identical lists: list1 = [1, 2, 3] and list2 = [1, 2, 3]. 
# Assign list3 = list1. Use == and is to compare list1 with list2, and list1 with list3. 
# Explain the differences in output.

list1 = [1,2,3]
list2 = [1,2,3]

list3 = list1

# this wil display true cos this comapres the value of the objects neglecting if they share the same address
print(list1 == list2)

# this wil display false cos the objects share different address
print(list1 is list2)


print(list1 == list3)
print(list3 is list1)


# Bitwise Masking: 
# Given an integer status code (e.g., status = 0b1011), use the bitwise AND (&) operator with a mask to check 
# if the 3rd bit (from the right, 0-indexed) is set to 1.

# Hint: The 3rd bit from the right has a binary value of 0b1000 (which is decimal 8). 
# Try using that as your mask!


status = 0b1011  # (In decimal, this is 11)

# The mask to isolate Bit Position 3
mask = 0b1000    # (In decimal, this is 8)

# Apply the Bitwise AND operator
result = status & mask

print(f"Result in decimal: {result}")
print(f"Result in binary:  {bin(result)}")

status = 0b1011  # The code you are testing

is_bit_set = (status & mask) != 0

print(f"Is the 3rd bit set to 1? {is_bit_set}")


# Fast Multiplication and Division: 
# Take an integer variable num = 16. Use bitwise left-shift (<<) to multiply it by 4, 
# and bitwise right-shift (>>) to divide it by 8. Print the binary representations of the numbers before 
# and after shifting.

  
num = 16

print("--- 1. Original Number ---")
print(f"Decimal: {num}")
print(f"Binary:  {bin(num)}")  # 0b10000

print("\n--- 2. Left-Shift (Multiply by 4) ---")
# Shifting left by 1 multiplies by 2. 
# Shifting left by 2 multiplies by 4 (2^2).
multiply_result = num << 2
print(f"Decimal: {multiply_result}")
print(f"Binary:  {bin(multiply_result)}")  # 0b1000000

print("\n--- 3. Right-Shift (Divide by 8) ---")
# Shifting right by 1 divides by 2.
# Shifting right by 3 divides by 8 (2^3).
divide_result = num >> 3
print(f"Decimal: {divide_result}")
print(f"Binary:  {bin(divide_result)}")  # 0b10




#     Bitwise XOR Swapping: 
# Swap two integer variables x = 25 and y = 30 using only the bitwise XOR (^) 
# operator over three sequential operations without any extra variables.

x = 25
y = 30

print(f"Before swap: x = {x}, y = {y}")

# Step 1: Combine both numbers into x
x = x ^ y

# Step 2: Extract the original x into y
y = x ^ y

# Step 3: Extract the original y into x
x = x ^ y

print(f"After swap:  x = {x}, y = {y}")