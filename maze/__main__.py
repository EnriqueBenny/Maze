import random

from maze.game.casting.actor import Actor
from maze.game.directing.director import Director

def main():
    point = Actor()


"""Rules: player moves though the maze to the goal.
If the player touches a wall, the maze is reset, and the player loses a life.

Code from cycle and greed has been recycled."""