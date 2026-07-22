# Challenge 3: The Dynamic Safety Valve (While Loop, break, If-Else)
# Concepts Tested: while loops, infinite loops with safe exits, break, and complex condition checking.

# The Task: Write a function named simulate_pressure_sensor(readings) that takes a list of integer 
# sensor readings and simulates processing them sequentially using a while loop:

# Maintain an index tracker starting at 0.

# Continuously fetch readings. If a reading is exactly 999, trigger an emergency shutdown by executing a 
# break statement that exits the loop immediately.

# If a reading is negative (e.g., -1), print "Sensor Error Ignored" using an if-else block, skip processing it, 
# and move to the next index.

# For all other valid readings, accumulate them into a running total sum.

# Return the running total once the loop finishes or breaks.


def simulate_pressure_sensor(dataList):

    index = 0
    total = 0

    while index < len(dataList):

        number = dataList[index]

        if number == 999:
            print("triggerring an emergency shutdown ")
            break

        else:
            if number < 0:
             print("Sensor Error Ignored")

            else:
             total += number

        index += 1

    return total

print(simulate_pressure_sensor([10, 20, -1, 30, 999, 40]))  # 60
print(simulate_pressure_sensor([5, 5, 5]))                   # 15
print(simulate_pressure_sensor([-1, -1, -1]))   