#Mod10_ex4

import random

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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)
    def print_status(self):
        print(f"\nRace: {self.name}")
        print(f"{'Registration':<15}"
              f"{'Max speed':<15}"
              f"{'Current speed':<15}"
              f"{'Distance (km)'}")
        for car in self.cars:
            print(
                f"{car.registration_number:<15}"
                f"{car.maximum_speed:<15}"
                f"{car.current_speed:<15}"
                f"{car.travelled_distance:.1f}")
    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False
cars = []

for i in range(1, 11):
    maximum_speed = random.randint(100, 200)
    car = Car(f"ABC-{i}", maximum_speed)
    cars.append(car)
race = Race("___GRAND DEMOLITION DERBY___", 8000, cars)
hours = 0

while not race.race_finished():
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        race.print_status()
race.print_status()