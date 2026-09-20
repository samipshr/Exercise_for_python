#Mod10_ex01

class elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom
    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print("Elevator is now on floor:", self.current_floor)
    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print("Elevator is now on floor:", self.current_floor)
    def go_to_floor(self, floor):
        if floor < self.bottom or floor > self.top:
            print("Invalid floor")
            return
        
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()

h = elevator(0, 10)
h.go_to_floor(5)
print("Going back to the bottom floor.")
h.go_to_floor(1)
