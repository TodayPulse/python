import payment

def payment_logger(message):
    print (f"[LOG TELEMETRY] : {message}")


if __name__ == "__main__":
    payment.pay_slip(logger_func = payment_logger)