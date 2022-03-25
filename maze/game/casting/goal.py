from game.casting.actor import Actor
from game.shared.point import Point
import constants
class Goal(Actor):

    def __init__(self):
        """Handles the Goal segment.
        """
        super().__init__()
        # Basicly an actor with a permanent position in the bottom right and text of G
        self._position = Point(39* constants.CELL_SIZE,19* constants.CELL_SIZE)
        self._text = "G"