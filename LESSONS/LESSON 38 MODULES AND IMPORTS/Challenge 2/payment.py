from notifications import notify


def pay_slip(logger_func):
    print(f"Getting payment slip")

    notify("Emmanuel", "$5000", logger_callback=logger_func)

