import constants

import random

from game.casting.cast import Cast
from game.casting.actor import Actor
from game.directing.director import Director
from game.shared.color import Color
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService

"""Rules: player moves though the maze to the goal.
If the player touches a wall, the maze is reset, and the player loses a life.
Code from greed has been recycled."""


def main():
    cast = Cast()

    points = Actor()
    points.set_text("")
    points.set_font_size(FONT_SIZE)
    points.set_color(WHITE)
    points.set_position(Actor(CELL_SIZE, 0))
    cast.add_actor("points", points)

    # create the robot
    x = 1
    y = 1
    points = Actor(x, y)


    # Calling main
    if __name__ == "__main__":
        main()


