class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal is speaking")

    def info(self):
        print(f"{self.name} is an animal")   # Default info


class Dog(Animal):  # child class dog inherits Animal
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("The dog barks")

    def info(self):
        print(f"{self.name} is a loyal dog")


class Cat(Animal):  # child class cat inherits Animal
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("The cat meows")

    def info(self):
        print(f"{self.name} is a curious cat")


# multilevel inheritance
class Puppy(Dog):  # inherits from Dog → Animal
    def speak(self):
        print("The puppy is growling")

    def info(self):
        print(f"{self.name} is a playful puppy")


class Kitten(Cat):  # inherits from Cat → Animal
    def speak(self):
        print("The kitten is hissing")

    def info(self):
        print(f"{self.name} is a cute kitten")


# Polymorphism in action
animals = [Dog("Bosco"), Cat("Puscat"), Puppy("Puppy"), Kitten("Jenn")]

for a in animals:
    a.speak()   # polymorphic behavior
    a.info()    # polymorphic behavior
    print("----")
