import constants

from game.casting.cast import Cast
from game.casting.actor import Actor
from game.casting.wall import Wall
from game.casting.goal import Goal
from game.casting.player import Player
from game.directing.director import Director
from game.shared.color import Color
from game.shared.point import Point
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

"""Rules: player moves though the maze to the goal.
If the player touches a wall, the maze is reset, and the player loses a life.
Code from greed has been recycled."""


def main():
    cast = Cast()
    cast.add_actor("wall", Wall())
    cast.add_actor("player", Player())
    cast.add_actor("goal", Goal())

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)


# Calling main
if __name__ == "__main__":
    main()


