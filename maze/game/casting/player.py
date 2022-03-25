from game.casting.actor import Actor
from game.shared.point import Point
import constants
class Player(Actor):

    def __init__(self):
        super().__init__()
        self._position = Point(0* constants.CELL_SIZE,0 * constants.CELL_SIZE)
        self._text = "@"
        #self._text = """
        # O 
        #/|\\
        #/ \\
        #"""