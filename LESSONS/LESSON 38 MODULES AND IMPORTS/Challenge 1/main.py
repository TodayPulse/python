import brewery
import inventory

def enterprsie_logger(message):
    print(f"[LOG TELEMETRY] : {message}")

if __name__ == "__main__":
    brewery.brew_coffee(logger_func = enterprsie_logger)