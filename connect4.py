import tkinter as tk
import random


class Connect4:

    def __init__(self):
        pass


class Board:

    def __init__(self):
        pass


class Red:

    def __init__(self):
        pass


class Yellow:

    def __init__(self):
        pass


def engine():
    pass


rows = [i for i in range(1, 7)]
columns = [i for i in range(1, 8)]
# Useful Links

# http://blog.gamesolver.org/solving-connect-four/01-introduction/
# https://towardsdatascience.com/creating-the-perfect-connect-four-ai-bot-c165115557b0
# https://tromp.github.io/c4/c4.html
# https://github.com/lhorrell99/connect-4-solver/blob/master

# 4531985219092 number of possible connect 4 positions
# Use notation of the position based on which columns you have used for example 4344
# if a number is repeated more than 6 times it is an invalid sequence of numbers
# it will tell you the best column to place in and the evaluation of the position for example if red
# is winning it will say +3 or +5 if it's crushing. If yellow are winning it will be -3 or -5.
# And 0 if it's a drawing position
# for example with 4455 red can win in 2 moves
