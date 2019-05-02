# python-rock-paper-scissors
A simple Python program that plays the classic game of Rock, Paper, Scissors

# Prerequisites
This game utilzies Python's PrettyTable to tabulate score, so you need to make sure that it is installed before running.
```bash
pip install PTable

# if using Python 3 you might have to do is like so:
pip3 install PTable
```

# How to Play
The game asks for various inputs, all you need to do is read them and answer with the corresponding values.

There are currently two game choices:
 - You vs. Computer
 - You vs. Player
 
 You can play different lengths of games by specifying `more` when prompted. The default is best 2/3 games.
 
 There is also a line in the `main.py` file for Windows users to keep track of score if you are playing it there. 
 Otherwise this defaults to a UNIX/LINUX platform for file location.
 
 To run the program you can copy the `main.py` source code and put it in your own file, or you can clone the repo.
 Either way once you have the file or its contents, simply just run it using python:
 ```bash
 python ./main.py
 
 # note if using Python 3 you might have to run it like so:
 python3 ./main.py
 ```
 
 # Problems or Features
 If you find a bug, or something you would like added, please feel free to suggest it as an issue.
