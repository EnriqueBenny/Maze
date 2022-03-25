from game.casting.actor import Actor
from game.shared.point import Point
import constants
class Player(Actor):

    def __init__(self):
        super().__init__()
        self._position = Point(10* constants.CELL_SIZE,10 * constants.CELL_SIZE)
        self._text = "O"
        #self._text = """
        # O 
        #/|\\
        #/ \\
        #"""