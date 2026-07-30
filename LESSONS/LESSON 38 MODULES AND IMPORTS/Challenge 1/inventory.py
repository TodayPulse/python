

def deduct(item,quantity, logger_callback = None):
    print(f"{quantity} of {item} is being drained from the machine")

    if logger_callback:
        logger_callback(f"Quantity of {item} deducted from the machine is {quantity}")

    return True
