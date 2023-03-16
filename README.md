# MachEight Coding Challenge


This repository contains the solution to MachEight's coding challenge. The main objective of the task was to _"find pairs of integers from a list that sum to a given value"_ given a series of numbers and a target number. This solution took a similar approach to the one illustrated in the instructions.

To accomplish the task and make the evaluation process simpler, three files have been provided in this repository: a [Makefile](./Makefile), a [Python module](./task.py), and this README file.


## Installation

To install, run `make` in the terminal.

A Makefile has been provided to execute the commands provided in the instructions. There are no additional steps required to run it smoothly.

The makefile will prepare the environment by changing the file name, assigning the correct permissions, and moving it to the appropriate folder. It will also provide feedback on what it is doing and notify you when it is finished, as well as provide usage instructions.

If it is not working, please make sure that you have the correct task.py file. If you do, simply run:

```
python3 task.py list_of_numbers target_number
```
Example usage:
```
python3 task.py 1,9,5,0,20,-4,12,16,7 12
```

## Usage
To use the application, run the following command in the terminal:

```
app list_of_numbers target_number
```

Example usage:
```
app 1,9,5,0,20,-4,12,16,7 12
```

If the app is not working, please refer back to the [Installation](#installation) section for further instructions.
