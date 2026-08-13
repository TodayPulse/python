# Task: Given a list of cup prices tray = [5.00, 2.00, 4.50, 3.50], 
# manually write out the state of the list after just one complete pass of
# Bubble Sort (comparing adjacent elements and bubbling the largest value to the right). 
# Write a short script that performs this single pass and prints the result.

# Goal: Trace the mechanics of how Bubble Sort moves large elements toward the end step-by-step.

tray = [5.00, 2.00, 10.50, 3.50]

length = len(tray)

for i in range(length-1):
    if tray[i] > tray[i+1]:
        tray[i],tray[i+1] = tray[i+1], tray[i]

print(tray)