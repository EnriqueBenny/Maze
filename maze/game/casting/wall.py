import constants
from game.casting.actor import Actor
from game.shared.point import Point
class Wall(Actor):

    def __init__(self):
        """Handles Wall segments"""
        super().__init__()
        self._segments = []
        self._create_segments()
        
    def get_segments(self):

        return self._segments

    def _create_segments(self):
        for row in range(constants.ROW_COUNT):
            for column in range(constants.COLUMN_COUNT):
                if constants.ROWS[row][column] == 0:
                    position = Point(column*constants.CELL_SIZE, row*constants.CELL_SIZE)

                    segment = Actor()
                    segment.set_position(position)
                    segment.set_text("W")
                    segment.set_color(constants.RED)
                    
                    self._segments.append(segment)