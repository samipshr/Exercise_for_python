#Mod9-ex1
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

car = Car("ABC-123", 142)

print(f"registration number: {car.registration_number}, maximum speed: {car.maximum_speed}km/h")
print(f"current speed ={car.current_speed}km/h, travelled distance = {car.travelled_distance}km")