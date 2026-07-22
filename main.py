def simulate_pressure_sensor(readings):
    index = 0
    total = 0

    while index < len(readings):
        reading = readings[index]

        if reading == 999:
            break
        else:
            if reading < 0:
                print("Sensor Error Ignored")
            else:
                total += reading

        index += 1

    return total


# --- Example usage ---
print(simulate_pressure_sensor([10, 20, -1, 30, 999, 40]))  # 60
print(simulate_pressure_sensor([5, 5, 5]))                   # 15
print(simulate_pressure_sensor([-1, -1, -1]))                 # 0