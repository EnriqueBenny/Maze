from game.scripting.action import Action
from game.shared.point import Point
import constants

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # stores the player and goal from the cast as a variable
        player = cast.get_first_actor("player")
        goal = cast.get_first_actor("goal")
        # collecting the single actor wall
        walls = cast.get_first_actor("wall")
        # grabbing the segments from the actor wall
        segments = walls.get_segments()
        

        # The game ending message that hasnt been created
        message = cast.get_actors("message")

        # clears the buffer then draws the actors and flushes the buffer
        self._video_service.clear_buffer()
        self._video_service.draw_actor(player)
        self._video_service.draw_actors(segments)
        self._video_service.draw_actor(goal)
        self._video_service.draw_actors(message,True)
        self._video_service.flush_buffer()