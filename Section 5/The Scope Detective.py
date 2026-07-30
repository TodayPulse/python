# The Scope Detective (Variable Scopes)
# Concepts Tested: Local vs global scope, the `global` keyword, enclosing scope, the
# `nonlocal` keyword, and LEGB resolution order.

# The Task: Write a function `scope_report()` that demonstrates all four scope levels:
#   1. Define a global variable `counter = 0` outside any function.
#   2. Inside scope_report(), define a nested function `increment_global()` that uses the
#      `global` keyword to increment the outer `counter` by 1 each time it's called.
#   3. Inside scope_report(), define a local variable `local_message = "local"`, then define
#      a nested function `modify_enclosing()` that uses `nonlocal` to change
#      `local_message` to "modified by enclosing scope".
#   4. Call increment_global() three times, then call modify_enclosing() once.
#   5. Return a dictionary showing the final state: {"global_counter": counter,
#      "local_message": local_message}.
#   6. Bonus: Explain (as a comment) what would happen if you removed the `global` keyword
#      from increment_global() and tried to do `counter += 1` — what error occurs and why.



def scope_report():
    counter = 0
    
    def increment_global():
        global counter += 1
