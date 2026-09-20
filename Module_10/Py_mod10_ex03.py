#Mod10_ex3

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom
    def floor_up(self):
        self.current_floor += 1
        print("Current floor:", self.current_floor)
    def floor_down(self):
        self.current_floor -= 1
        print("Current floor:", self.current_floor)
    def go_to_floor(self, floor):
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()


class Building:

    def __init__(self, bottom, top, number_of_elevators):
        self.elevators = []
        for i in range(number_of_elevators):
            self.elevators.append(Elevator(bottom, top))
    def run_elevator(self, elevator_number, destination):
        self.elevators[elevator_number].go_to_floor(destination)
    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(elevator.bottom)

building = Building(0, 20, 5)
print(f"Elevator 1:")
building.run_elevator(0, 5)
print(f"Elevator 2:") 
building.run_elevator(1, 7)
print(f"Elevator 3:")
building.run_elevator(2, 10)
print(f"Elevator 4:")
building.run_elevator(3, 18)
print(f"Elevator 5:")
building.run_elevator(4, 11)

print("FIRE! EVACUATION. ALL ELEVATORS WILL GO TO THE BOTTOM FLOOR")
building.fire_alarm()