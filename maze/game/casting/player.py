from game.casting.actor import Actor
from game.shared.point import Point
import constants
class Player(Actor):

    def __init__(self):
        """Handles the Player actor
        """
        super().__init__()
        # Basicly an actor with a permanent position in the top left and text of @
        self._position = Point(0* constants.CELL_SIZE,0 * constants.CELL_SIZE)
        self._text = "@"