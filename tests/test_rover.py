import pytest

from lib.rover import Rover
from utils.exceptions import OutOfPlateauError


def run_rover(data):
    """
    Initialize Rover and move based on instructions.
    """
    rover = Rover(
        plateau=data["plateau"],
        rover_name=data["rover_name"],
        position=data["position"]
    )
    for instruction in data["instructions"]:
        rover.send_command(instruction)
    return rover.get_final_position()


def test_rover():
    """
    Test Rover for pass and exception.
    """
    test_data_pass = [
        {
            "plateau": [10, 10],
            "rover_name": "Rover3",
            "position": [3, 8, 'W'],
            "instructions":"MRMLR",
            "result":"Rover3:2 9 N"
        },
        {
            "plateau": [7, 7],
            "rover_name": "Rover5",
            "position": [5, 3, 'N'],
            "instructions":"MMRR",
            "result":"Rover5:5 5 S"
        },
        {
            "plateau": [11, 11],
            "rover_name": "Rover7",
            "position": [0, 1, 'E'],
            "instructions":"MRMLMR",
            "result":"Rover7:2 0 S"
        }
    ]
    test_data_exception = [
        {
            "plateau": [10, 10],
            "rover_name": "Rover1",
            "position": [0, 9, 'N'],
            "instructions":"LMLMLR"
        },
        {
            "plateau": [10, 10],
            "rover_name": "Rover2",
            "position": [7, -2, 'S'],
            "instructions":"RLMRMR"
        },
        {
            "plateau": [1, 1],
            "rover_name": "Rover4",
            "position": [-4, 2, 'E'],
            "instructions":"RRMM"
        },
        {
            "plateau": [10, 20],
            "rover_name": "Rover6",
            "position": [9, -2, 'W'],
            "instructions":"LLRR"
        }
    ]
    for data in test_data_pass:
        final_position = run_rover(data)
        assert final_position == data["result"]

    with pytest.raises(OutOfPlateauError):
        for data in test_data_exception:
            run_rover(data)
