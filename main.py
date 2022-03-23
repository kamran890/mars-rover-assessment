from lib.data_handler import RoverDataHandler
from lib.rover import Rover

import sys


def handle_rover(file_name):
    """
    Get instructions for each rover from input file. Create Rover object and send the instructions.
    Get the final position of Rover and print it.
    """
    data_handle = RoverDataHandler(input_file=file_name)

    for entry in data_handle.get_entries():
        rover = Rover(plateau=entry["plateau"], rover_name=entry["rover_name"], position=entry["position"])
        for instruction in entry["instructions"]:
            rover.send_command(instruction)
        print(rover.get_final_position())


if __name__ == "__main__":
    """
    Call the rover handler
    """
    file_name = sys.argv[-1]
    handle_rover(file_name)
