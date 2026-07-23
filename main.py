class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} can walk")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name,breed)
        # self.breed = breed

    def sound(self):
        print(f"Name: {self.name} \nDog Breed: {self.breed} \nCan Bark: True")


dog1 = Dog("Lu", "Labrador")
dog1.walk()
dog1.sound()