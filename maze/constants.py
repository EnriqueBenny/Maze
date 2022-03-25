from multiprocessing.context import SpawnContext
from game.shared.color import Color


COLUMNS = 40
ROWS = 20
CELL_SIZE = 15
MAX_X = 900
MAX_Y = 600
FRAME_RATE = 15
FONT_SIZE = 15
CAPTION = "Maze"
SNAKE_LENGTH = 8
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)

# maze (w, is a wall, s, is a space, G is goal):
s = "Space"
w = "Wall"
G = "Goal"
first_line = [s, s, s, s, s, w, s, s, s, w, s, s, s, s, s, s, s, s, s, w, w, s, s, s, s, w, s, s, s, s, s, s, s, s, s, s, s, s, s, s]
second_line = [w, s, w, w, s, w, s, w, s, w, s, w, w, s, w, w, w, w, s, s, s, s, w, w, s, w, w, w, w, w, w, s, w, s, w, s, w, w, w, w]
third_line = [w, s, s, s, w, w, s, w, s, s, s, w, w, s, s, s, w, w, s, w, w, w, w, w, w, w, s, s, s, s, s, s, w, s, w, s, s, s, s, s]
fourth_line = [w, w, w, s, s, s, s, w, w, w, w, w, w, s, w, s, w, w, s, s, s, s, s, s, w, w, s, w, w, w, w, w, w, s, w, w, w, w, s, w]
fifth_line = [w, s, s, s, w, w, w, w, w, s, s, s, w, s, w, s, s, w, s, w, w, w, w, s, w, w, s, w, s, s, s, s, s, s, w, s, s, s, s, w]
sixth_line = [s, s, w, w, w, s, s, s, s, s, w, w, w, s, w, w, s, s, s, s, s, w, s, s, s, s, s, w, s, w, w, w, w, w, s, s, w, w, w, w]
seventh_line = [w, s, s, w, w, w, w, w, w, s, w, w, w, s, w, w, s, w, w, w, s, w, s, w, w, w, w, w, s, w, w, s, s, s, w, s, w, w, w, s]
eigth_line = [w, w, s, w, s, s, s, s, w, s, s, s, w, s, w, w, s, w, w, w, s, w, s, w, s, s, s, w, s, w, s, s, w, s, w, s, s, s, s, s]
ninth_line = [s, s, s, w, s, w, w, s, w, w, w, s, w, s, w, w, s, w, w, w, s, w, s, w, w, s, w, w, s, s, s, w, w, s, s, w, w, w, w, s]
tenth_line = [s, w, s, w, s, w, w, s, s, s, s, s, w, s, w, w, s, s, s, s, s, s, s, w, w, s, s, w, w, w, w, s, s, w, s, s, s, s, w, w]
eleventh_line = [s, w, w, w, s, s, w, w, w, w, w, w, w, s, w, w, w, w, w, s, w, w, w, w, w, w, s, w, w, w, w, w, s, w, w, w, w, s, s, s]
twelfth_line = [s, s, w, w, w, s, s, s, w, s, s, s, s, s, s, s, s, s, w, s, s, s, s, s, w, w, s, s, s, s, s, s, s, s, s, s, w, w, w, s]
thirteenth_line = [w, s, s, w, w, s, w, s, w, w, w, w, w, s, w, w, w, s, w, w, w, s, w, s, s, s, s, w, w, w, w, w, w, w, w, w, w, w, w, s]
fourteenth_line = [w, w, w, s, w, s, w, s, w, s, s, s, w, s, w, w, w, s, w, w, w, s, w, w, s, w, s, w, s, s, s, s, s, s, s, s, s, s, s, s]
fifteenth_line = [s, s, w, s, w, s, w, s, s, s, w, s, w, s, s, s, s, s, s, s, w, s, w, w, s, w, s, w, s, w, w, w, w, w, w, s, w, w, w, w]
sixteenth_line = [w, s, w, s, w, s, w, s, w, w, w, s, w, w, w, w, w, w, w, s, s, s, s, w, s, w, s, w, s, w, s, s, s, s, w, s, s, s, s, w]
seventeenth_line = [s, s, s, s, w, s, w, s, w, w, w, s, w, s, s, s, s, s, w, s, w, w, s, w, s, w, s, w, s, s, s, w, w, s, w, w, w, w, s, s]
eighteenth_line = [s, w, w, w, w, s, w, s, w, w, s, s, w, s, w, w, w, s, w, s, w, w, s, w, s, w, s, w, w, w, w, w, w, s, w, w, w, w, w, s]
ninteenth_line = [s, s, s, s, w, s, w, s, s, w, w, s, s, s, s, w, w, s, w, s, w, w, s, s, s, s, s, s, s, s, s, s, w, s, s, s, s, s, w, s]
twenty_line = [w, s, w, s, w, w, w, s, w, w, w, s, w, w, s, w, w, s, w, s, w, w, w, w, w, w, w, w, w, w, w, s, w, w, w, w, w, s, s, G]
#w, s, w, s, s, s, s, s, s, s, s, s, s, w, s, s, s, s, w, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, w, w, s, G]