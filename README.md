## Instructions

* Pre-requisite
```
Python 3.6.9
```

* Install virtual environment
```bash
python3 -m venv .env
```

* Activate virtual envionment
```bash
source .env/bin/activate
```

* Install dependencies
```bash
pip3 install -r requirements.txt
```

* Run code
```bash
python3 main.py input.txt
```

* Run unit tests
```bash
python3 -m pytest
```

## Mars Rover

A squad of robotic rovers are to be landed by NASA on a plateau on Mars.

This plateau, which is curiously rectangular, must be navigated by the rovers so that their on board cameras can get a complete view of the surrounding terrain to send back to Earth.

A rover's position is represented by a combination of an x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot.

'M' means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).

Input:

Configuration Input: The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.

Per Rover Input:

Input 1: Landing co-ordinates for the named Rover. The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover's orientation.

Input 2: Navigation instructions for the named rover. i.e a string containing ('L', 'R', 'M').

Test Input:
```
Plateau:5 5
Rover1 Landing:1 2 N
Rover1 Instructions:LMLMLMLMM
Rover2 Landing:3 3 E
Rover2 Instructions:MMRMMRMRRM
```

Expected Output:
```
Rover1:1 3 N
Rover2:5 1 E
```
## Task:

Develop a command line app that can take the various inputs from the command line and generate the desired outputs. The application must accept a sequence of inputs from the command line or a file. Example input from file:
```
$ app input.txt
Rover1:1 3 N
Rover2:5 1 E
$
```
See `input.txt` in this repo for a sample test input.

### Evaluation and Submission Notes

#### Expectations:

- App should be working (We may build and run your app on MacOS or Ubuntu).
- Code should be modular and readable
- Unit tests
- Your choice of language is one with which you are comfortable
- Instructions on how to build and run the application. 
- Include what versions of software are needed to build your app.
- Write the code knowing that you'll need to enhance it in the next part of the interview process.
- Be prepared to give a brief overview on your design decisions.

- **Don't hesitate to ask us for clarifications**
