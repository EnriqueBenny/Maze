import constants

from game.casting.cast import Cast
from game.casting.actor import Actor
from game.casting.wall import Wall
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
If the player touches a wall, the maze is reset, and the player loses a life."""


def main():
    # sets up the cast and adds 1 player and 1 goal object to it. 
    cast = Cast()

    # Creates the player actor
    player = Actor()
    player.set_position(Point(0* constants.CELL_SIZE,0 * constants.CELL_SIZE))
    player.set_text("@")

    # Creates the goal actor
    goal = Actor()
    goal.set_position(Point(39* constants.CELL_SIZE,19 * constants.CELL_SIZE))
    goal.set_text("G")

    # Adds the actors to the cast
    cast.add_actor("player", player)
    cast.add_actor("goal", goal)

    # creates ONE wall object for cast. the wall segments are done in wall.py
    cast.add_actor("wall", Wall())

    # Get the services for the actions and director
    keyboard_service = KeyboardService()
    video_service = VideoService()

    # Creates the script for the director and adds the 4 actions into three catagories
    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    # initializes the game with the cast and script. 
    director = Director(video_service)
    director.start_game(cast, script)


# Calling main
if __name__ == "__main__":
    main()


