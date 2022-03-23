class OutOfPlateauError(Exception):
    """
    Exception raised when Rover moves outside of Plateau.
    """

    def __init__(self, message="Rover is out of Plateau."):
        super().__init__(message)


class InvalidFileError(Exception):
    """
    Exception raised when invalid file is provided.
    """

    def __init__(self, message="Provide valid input file."):
        super().__init__(message)
