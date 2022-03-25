import constants
from game.casting.actor import Actor
from game.shared.point import Point
class Wall(Actor):
    """One wall actor that is split between muliple segments. 
     Each segment is in the attribute list self._segments
     These segments are created with the method that uses a premade map in constants."""

    def __init__(self):
        """Handles Wall segments"""
        super().__init__()
        # self._segments will hold all segments but for now it is empty
        self._segments = []
        # This calls the method in the initiaziation which creates segment actors and adds them to the list.
        self._create_segments()
        
    def get_segments(self):
        """Collects the segments from the wall actor"""
        return self._segments

    def _create_segments(self):
        # Grabs each row one at a time
        for row in range(constants.ROW_COUNT):
            # within the row grab the column one at a time
            for column in range(constants.COLUMN_COUNT):
                # Checks if the (column,row) of the map in constants is a 0
                if constants.ROWS[row][column] == 0:
                    # collects the (column,row) in the Point system
                    position = Point(column*constants.CELL_SIZE, row*constants.CELL_SIZE)
                    
                    # Creates an actor
                    segment = Actor()
                    segment.set_position(position)
                    segment.set_text("W")
                    segment.set_color(constants.RED)
                    # Adds the actor to the segments list
                    self._segments.append(segment)