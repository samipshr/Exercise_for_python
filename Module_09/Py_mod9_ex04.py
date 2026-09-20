#mod9_ex04

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

cars = []

for i in range(1, 11):
    maximum_speed = random.randint(100, 200)
    car = Car(f"ABC-{i}", maximum_speed)
    cars.append(car)

while True:
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)
        winner = False
    for car in cars:
        if car.travelled_distance >= 10000:
            winner = True
            break
    if winner:
        break

print(f"{'Registration':<15}{'Max speed':<15}{'Current speed':<15}{'Distance'}")

for car in cars:
    print(
        f"{car.registration_number:<15}"
        f"{car.maximum_speed:<15}"
        f"{car.current_speed:<15}"
        f"{car.travelled_distance:.1f}"
    )

