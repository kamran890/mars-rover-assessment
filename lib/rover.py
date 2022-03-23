from utils.direction import DIRECTION_MAP, DIRECTION_COMMANDS
from utils.exceptions import OutOfPlateauError


class Rover:
    """
    A module to represent a Rover.
    """
    def __init__(self, plateau, rover_name, position):
        self.plateau = plateau
        self.rover_name = rover_name
        self.position = position
        self.step_f = {
            "E": self.handle_east,
            "W": self.handle_west,
            "N": self.handle_north,
            "S": self.handle_south
        }

    def send_command(self, command):
        """
        Send a command to Rover.
        """
        if command == "M":
            self.step()
        elif command in DIRECTION_COMMANDS:
            self.change_direction(command)

    def step(self):
        """
        Move one step.
        """
        self.step_f[self.position[2]]()
        if not self.is_within_plateau():
            raise OutOfPlateauError

    def change_direction(self, command):
        """
        Change direction of Rover.
        """
        self.position[2] = DIRECTION_MAP[self.position[2]][command]

    def get_position(self):
        """
        Get current position of Rover.
        """
        return self.position

    def get_final_position(self):
        """
        Get final position of Rover.
        """
        self.position[0] = str(self.position[0])
        self.position[1] = str(self.position[1])
        self.position = " ".join(self.position)
        return f"{self.rover_name}:{self.position}"

    def handle_east(self):
        """
        Change direction when current direction is East.
        """
        self.position[0] = self.position[0] + 1

    def handle_west(self):
        """
        Change direction when current direction is West.
        """
        self.position[0] = self.position[0] - 1

    def handle_north(self):
        """
        Change direction when current direction is North.
        """
        self.position[1] = self.position[1] + 1

    def handle_south(self):
        """
        Change direction when current direction is South.
        """
        self.position[1] = self.position[1] - 1

    def is_within_plateau(self):
        """
        Check if Rover is within plateau
        """
        is_within_top_right = (
            self.position[0] <= self.plateau[0]
            and self.position[1] <= self.plateau[1]
        )
        is_within_bottom_left = self.position[0] >= 0 and self.position[1] >= 0
        return is_within_top_right and is_within_bottom_left
