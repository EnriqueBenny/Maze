from game.casting.actor import Actor
from game.shared.point import Point
import constants
class Goal(Actor):

    def __init__(self):
        """Handles Goal segments
        """
        super().__init__()
        self._position = Point(-10* constants.CELL_SIZE,-10 * constants.CELL_SIZE)
        self._text = "G"