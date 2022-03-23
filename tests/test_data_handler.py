from lib.data_handler import RoverDataHandler


def test_data_handler():
    """
    Test input file data handler.
    """
    data_handle = RoverDataHandler(input_file="input.txt")

    test_data = {
        "Rover1": {"position": [1, 2, "N"], "instructions": "LMLMLMLMM"},
        "Rover2": {"position": [3, 3, "E"], "instructions": "MMRMMRMRRM"}
    }
    for entry in data_handle.get_entries():
        assert entry["plateau"] == [5, 5]
        assert entry["position"] == test_data[entry["rover_name"]]["position"]
        assert entry["instructions"] == test_data[entry["rover_name"]]["instructions"]
