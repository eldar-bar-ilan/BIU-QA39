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

# create 2 objects of Car class
car1 = Car(101, "Ford", 0)
car2 = Car(102, "Toyota", 20)

car1.drive(100)


print(f"Car[number={car1.number}, make={car1.make}, speed={car1.current_speed}]")
print(f"Car[number={car2.number}, make={car2.make}, speed={car2.current_speed}]")

car1.stop()
car2.stop()
print(f"Car[number={car1.number}, make={car1.make}, speed={car1.current_speed}]")
print(f"Car[number={car2.number}, make={car2.make}, speed={car2.current_speed}]")



