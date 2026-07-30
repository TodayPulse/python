import time

def timer_dec(base_fn):
    def enhanced_fn(*args, **kwargs):
        start = time.time()
        result = base_fn(*args, **kwargs )          # Capture the original function's result
        end = time.time()
        print(f"Time taken: {end - start} seconds")
        return result               # Return the result so it isn't lost
        
    return enhanced_fn              # <--- THIS WAS MISSING! It returns the wrapper function.

@timer_dec
def brew_tea(tea_type, steep_time):
    print(f"Brewing tea... Tea_type is \n {tea_type} \n Steep_time is {steep_time}")
    time.sleep(1)
    print("Tea is ready!")

@timer_dec
def make_bread():
    print("Baking bread...")
    time.sleep(1)
    print("Bread is baked!")

# Applying the decorator manually (or you could use @timer_dec above def brew_tea)
# brew_tea = timer_dec(brew_tea)

# Calling it now works correctly!
brew_tea("green", 1)
make_bread()