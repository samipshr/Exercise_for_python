class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
        self.speed = 0

    def acccelerate(self, value):
        self.speed += value

car = Car("ABC-123", 142)

print(
    f"registration number: {car.registration_number}, maximum speed: {car.maximum_speed}"
)

speed_1 = car.acccelerate(30)
speed_2 = car.acccelerate(70)
speed_3 = car.acccelerate(50)
accelerated_speed = speed_1 + speed_2 + speed_3
print(f"accelerated speed is: {accelerated_speed}")
brake = accelerated_speed - 200
print(f"usnig emergency brake acceleration is now:{brake}")
print(car.speed)
