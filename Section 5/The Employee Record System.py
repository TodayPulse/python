# The Employee Record System (Classes & Objects)
# Concepts Tested: Class definition, __init__, instance attributes vs class attributes,
# instance methods, and the __str__ dunder method.

# The Task: Write a class named Employee that:
#   1. Has a class attribute `company_name` shared by all instances, set to "TechCorp".
#   2. Has an __init__ that accepts `name` and `salary`, storing them as instance attributes.
#   3. Has a method `give_raise(amount)` that increases `self.salary` by `amount`.
#   4. Has a method `describe()` that returns a formatted string:
#      "Name works at CompanyName earning $Salary" (using the actual attribute values).
#   5. Implements __str__ so that print(employee_instance) outputs the same string as describe().
#   6. Bonus: add a class method `change_company(new_name)` that updates `company_name`
#      for ALL existing and future Employee instances at once.


class Employee:

    company_name = "TechCorp"

    def __init__(self, name , salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        return f"{self.name}'s salary has been raised by {amount} \n New Salary is now : ${self.salary}"

    def describe(self):
       return f"{self.name} works at {self.company_name} earning ${self.salary}"

    def __str__(self):
        return self.describe()

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name


employee1 = Employee("Emmanuel", 10000000)
print(employee1)
print(employee1.describe())

print(employee1.give_raise(506750))
print(employee1)

employee1.change_company("Devcrib")
print(employee1)