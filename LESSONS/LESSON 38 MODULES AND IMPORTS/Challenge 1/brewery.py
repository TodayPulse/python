from inventory import deduct

def brew_coffee(logger_func):
    print("Extracting from the machine")

    deduct("Cofee","10 cl", logger_callback=logger_func)

    print("Successfully extrected from the machine")

    