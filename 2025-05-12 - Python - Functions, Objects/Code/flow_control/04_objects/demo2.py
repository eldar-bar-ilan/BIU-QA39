# class definition
class Car:
    def __init__(self, number, make, current_speed):
        self.number = number
        self.make = make
        self.current_speed = current_speed

    def drive(self, speed):
        self.current_speed = speed

    def stop(self):
        self.current_speed = 0

    def __repr__(self):
        return f"Car[number={self.number}, make={self.make}, speed={self.current_speed}]"


# create 2 objects of Car class
car1 = Car(101, "Ford", 0)
car2 = Car(102, "Toyota", 20)

car1.drive(100)
print(car1)
print(car2)

car1.stop()
car2.stop()
print(car1)
print(car2)
