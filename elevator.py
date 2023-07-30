class Elevator:
    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.current_floor = 1
        self.is_moving = False

    def call_elevator(self, floor):
        if self.is_valid_floor(floor):
            if self.is_moving:
                print("Elevator is currently moving. Please wait.")
            else:
                self.move_to_floor(floor)

    def move_to_floor(self, floor):
        self.is_moving = True
        if floor > self.current_floor:
            for f in range(self.current_floor, floor + 1):
                print(f"Moving up... Floor {f}")
                self.current_floor = f
        else:
            for f in range(self.current_floor, floor - 1, -1):
                print(f"Moving down... Floor {f}")
                self.current_floor = f
        self.is_moving = False
        print("Elevator has arrived.")

    def open_doors(self):
        print("Opening doors...")
       

    def close_doors(self):
        print("Closing doors...")
      

    def is_valid_floor(self, floor):
        if 1 <= floor <= self.num_floors:
            return True
        else:
            print(f"Invalid floor. Please choose a floor between 1 and {self.num_floors}.")
            return False


def main():
    num_floors = 7  
    elevator = Elevator(num_floors)

    while True:
        print(f"\nCurrent floor: {elevator.current_floor}")
        command = input("Enter 'call', 'open', 'close', 'exit', or a floor number to call the elevator: ")

        if command == 'exit':
            print("Exiting the elevator simulation.")
            break
        elif command == 'call':
            floor = int(input("Enter the floor number to call the elevator: "))
            elevator.call_elevator(floor)
        elif command == 'open':
            elevator.open_doors()
        elif command == 'close':
            elevator.close_doors()
        else:
            floor = int(command)
            elevator.call_elevator(floor)


if __name__ == "__main__":
    main()
