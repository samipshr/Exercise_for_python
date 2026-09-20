#mod9_ex03

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def acccelerate(self, value):
        self.current_speed += value
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

car = Car("ABC-123", 142)

print(
    f"registration number: {car.registration_number}, maximum speed: {car.maximum_speed}"
)

car.acccelerate(30)
car.acccelerate(70)
car.acccelerate(50)

print(f"accelerated speed is: {car.current_speed}km/h")
brake = car.current_speed - 200
print(f"Using emergency brake, speed is now:{brake}")
print(f"Again speeding up to 60km/h")
print("\n")

car.acccelerate(60)
car.travelled_distance = 2000
car.drive(2.5)
print(f"Total Travelled distance is:{car.travelled_distance}km")
