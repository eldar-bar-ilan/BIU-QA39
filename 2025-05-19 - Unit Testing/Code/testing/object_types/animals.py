class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.energy_level = 100

    def bark(self):
        print(f"{self.name} says Woof")

    def walk(self, minutes):
        if self.energy_level >= minutes:
            print(f"{self.name} is walking")
            self.energy_level -= minutes
        else:
            print(f"{self.name} is too tired to walk")

    def rest(self, hours):
        self.energy_level += hours * 60


if __name__ == "__main__":
    # =============================================
    d1 = Dog("Luna", "Labrador")
    d2 = Dog("Miki", "Boxer")
    d1.bark()
    d2.bark()
    d2.walk(10)
    d1.walk(100)
    d1.walk(20)  # no energy
    d2.walk(20)
    d1.rest(2)
    d1.walk(30)
    print("=================")
