import time

class CoffeeMachine:
    def __init__(self, coffee_type):
        self.coffee_type = coffee_type
        print(f"⏳ Preparing {coffee_type} machine...")
    
    def __enter__(self):
        print(f"✅ {self.coffee_type} machine ready!")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"🧹 Cleaning {self.coffee_type} machine...")
        if exc_type:
            print(f"⚠️ Error occurred: {exc_val}")
        print("✅ Machine cleaned!")
        # Returning False re-raises exceptions, True suppresses them
        return False
    
    def make_coffee(self):
        print(f"☕ Making {self.coffee_type}...")
        time.sleep(0.5)
        return f"Here's your {self.coffee_type}!"

# Usage
with CoffeeMachine("Latte") as machine:
    result = machine.make_coffee()
    print(result)