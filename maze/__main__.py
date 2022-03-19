import random

from maze.game.casting.actor import Actor
from maze.game.directing.director import Director
from maze.game.shared.color import Color

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Maze"
WHITE = Color(255, 255, 255)
GREEN = Color(0,255,0)
RED = Color(255,0,0)
GEM_COUNT = 35
STONE_COUNT = 30

def main():
    points = Actor()
    points.set_text("")
    points.set_font_size(FONT_SIZE)
    points.set_color(WHITE)
    points.set_position(Actor(CELL_SIZE, 0))
    cast.add_actor("points", points)

    # create the robot
    x = int(MAX_X / 2)
    y = 570
    position = Actor(x, y)


"""Rules: player moves though the maze to the goal.
If the player touches a wall, the maze is reset, and the player loses a life.

Code from cycle and greed has been recycled."""