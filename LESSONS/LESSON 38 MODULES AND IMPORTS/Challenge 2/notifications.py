
def notify(name, amount, logger_callback = None):
    if logger_callback:
        logger_callback(f"{name} just made a payment of {amount}")

    return "SUCCESS"