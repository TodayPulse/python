# Task: Your colleague wrote a Bubble Sort inner loop, 
# but it crashes with an IndexError when it reaches the end of the counter tray. 
# Look at the snippet below and rewrite the loop range correctly so it never crashes:

# Fix this loop:
prices = [3.50, 4.00, 2.50]
for i in range(len(prices)-1):
    if prices[i] > prices[i + 1]:
        prices[i], prices[i + 1] = prices[i + 1], prices[i]



# # Task: Your colleague wrote a Bubble Sort inner loop, 
# # but it crashes with an IndexError when it reaches the end of the counter tray. 
# # Look at the snippet below and rewrite the loop range correctly so it never crashes:

# Fix this loop:
prices = [3.50, 4.00, 2.50]
for num in range(len(prices)):
    for i in range(0, len(prices)-num -1):
        if prices[i] > prices[i + 1]:
            prices[i], prices[i + 1] = prices[i + 1], prices[i]


print(prices)