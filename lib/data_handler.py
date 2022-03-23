from utils.exceptions import InvalidFileError


class RoverDataHandler:
    """
    A module to handle the input data of Rover.
    """
    def __init__(self, input_file):
        self.input_file = open(input_file)
        self.plateau = None
        self.rover_name = None
        self.position = None
        self.instructions = None

    def get_lines(self):
        """
        Get lines from input file.
        """
        lines = self.input_file.readlines()
        return lines

    def get_entries(self):
        """
        Extract data from each line.
        """
        for entry in self.get_lines():
            entry = entry.replace("\n", "")
            if "Plateau" in entry:
                self.plateau = entry.split(":")[1].split(" ")
                self.plateau = [int(i) for i in self.plateau]
            elif "Landing" in entry:
                self.rover_name = entry.split(":")[0].split(" ")[0]
                self.position = entry.split(":")[1].split(" ")
                self.position[0] = int(self.position[0])
                self.position[1] = int(self.position[1])
            elif "Instructions" in entry:
                self.instructions = entry.split(":")[1]
                yield {
                    "plateau": self.plateau,
                    "rover_name": self.rover_name,
                    "position": self.position,
                    "instructions": self.instructions
                }
            else:
                raise InvalidFileError
