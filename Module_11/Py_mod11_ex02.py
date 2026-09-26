#Mod11_ex02

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume

electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(185)
gasoline_car.accelerate(165)
electric_car.drive(3)
gasoline_car.drive(3)

print("Electric car:")
print("Registration:", electric_car.registration_number)
print("Maximum speed:", electric_car.maximum_speed, "km/h")
print("Battery capacity:", electric_car.battery_capacity, "kWh")
print("Kilometer counter:", electric_car.travelled_distance, "km")
print()

print("Gasoline car:")
print("Registration:", gasoline_car.registration_number)
print("Maximum speed:", gasoline_car.maximum_speed, "km/h")
print("Tank volume:", gasoline_car.tank_volume, "l")
print("Kilometer counter:", gasoline_car.travelled_distance, "km")