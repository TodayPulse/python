# The Vehicle Hierarchy (Inheritance)
# Concepts Tested: Base classes, subclasses, super(), method overriding, polymorphism, isinstance().

# The Task:
#   1. Write a base class `Vehicle` with __init__(self, make, model) and a method `describe()`
#      returning f"{make} {model}".
#   2. Write a subclass `Car` that inherits from `Vehicle`, adds a `num_doors` attribute via
#      its own __init__ (using super() to handle make/model), and OVERRIDES `describe()` to
#      append " with X doors" to the parent's output (call the parent version with super()
#      rather than rewriting the string from scratch).
#   3. Write a second subclass `ElectricCar` that inherits from `Car`, adds a `battery_range`
#      attribute, and overrides `describe()` again to append " and Y miles range", again
#      building on top of the parent class's describe() via super().
#   4. Write a function `print_all_descriptions(vehicles)` that loops through a mixed list of
#      Vehicle/Car/ElectricCar objects and prints each one's describe() — demonstrating
#      polymorphism (same method call, different behavior per class).
#   5. Bonus: write a check using isinstance() that confirms every ElectricCar is also a Car
#      and also a Vehicle.


class Vehicle:
    def __init__ (self, make, model):
        self.make = make
        self.model = model

    def describe(self):
          return f" Make: {self.make} ::: Model: {self.model}"

class Car(Vehicle):
     def __init__(self, make, model, num_doors):
          super().__init__(make,model)
          self.num_doors = num_doors

     def describe(self):
          return super().describe() + f" >>> with {self.num_doors} doors"
     
#   Write a second subclass `ElectricCar` that inherits from `Car`, adds a `battery_range`
#   attribute, and overrides `describe()` again to append " and Y miles range", again
#   building on top of the parent class's describe() via super().


class ElectricCar(Car):
     def __init__(self, make, model, num_doors, battery_range):
          super().__init__(make,model,num_doors)
          self.battery_range = battery_range

     def describe(self):
          return super().describe() + f" and {self.battery_range} miles range"


# Write a function `print_all_descriptions(vehicles)` that loops through a mixed list of
# Vehicle/Car/ElectricCar objects and prints each one's describe() — demonstrating
# polymorphism (same method call, different behavior per class).

def print_all_descriptions(vehicles):

     for vehicle in vehicles:
          print(vehicle.describe())



# --- Example usage ---
vehicles = [
    Vehicle("Generic", "Transport"),
    Car("Toyota", "Corolla", 4),
    ElectricCar("Tesla", "Model 3", 4, 300),
]

print_all_descriptions(vehicles)


tesla = ElectricCar("Tesla", "Model 3", 4, 300)

print(isinstance(tesla, ElectricCar))  # ?
print(isinstance(tesla, Car))          # ?
print(isinstance(tesla, Vehicle))      # ?