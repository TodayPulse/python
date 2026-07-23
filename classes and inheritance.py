# Python Classes and Objects


class Student:
    def __init__(self, id_number, name, age):
        self.id_number = id_number
        self.name = name
        self.age = age


    def student_greeting(self, greetings):
        print(f"Hello {self.name}, {greetings}")


student1 = Student(3232, "Olowu Emmanuel", 26)
student1.student_greeting("welcome back Boy!")



# Python Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} as an animal can walk")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


    def bark(self):
       name = self.name.lower()
       if name != "dog":
           print("This only checks for dog please")
           return

       print(f"Name: {self.name} \nDog Breed: {self.breed} \nCan Bark: True")

dog1 = Dog("Dkog", "labrado")
dog1.walk()
dog1.bark()
       