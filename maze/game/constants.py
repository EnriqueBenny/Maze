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

# maze (w is a wall, s is a space, G is goal):
"""
s s s s s w s s s w s s s s s s s s s w w s s s s w s s s s s s s s s s s s s s
w s w w s w s w s w s w w s w w w w s s s s w w s w w w w w w s w s w s w w w w
w s s s w w s w s s s w w s s s w w s w w w w w w w s s s s s s w s w s s s s s
w w w s s s s w w w w w w s w s w w s s s s s s w w s w w w w w w s w w w w s w
w s s s w w w w w s s s w s w s s w s w w w w s w w s w s s s s s s w s s s s w
s s w w w s s s s s w w w s w w s s s s s w s s s s s w s w w w w w s s w w w w
w s s w w w w w w s w w w s w w s w w w s w s w w w w w s w w s s s w s w w w s
w w s w s s s s w s s s w s w w s w w w s w s w s s s w s w s s w s w s s s s s
s s s w s w w s w w w s w s w w s w w w s w s w w s w w s s s w w s s w w w w s
s w s w s w w s s s s s w s w w s s s s s s s w w s s w w w w s s w s s s s w w
s w w w s s w w w w w w w s w w w w w s w w w w w w s w w w w w s w w w w s s s
s s w w w s s s w s s s s s s s s s w s s s s s w w s s s s s s s s s s w w w s
w s s w w s w s w w w w w s w w w s w w w s w s s s s w w w w w w w w w w w w s
w w w s w s w s w s s s w s w w w s w w w s w w s w s w s s s s s s s s s s s s
s s w s w s w s s s w s w s s s s s s s w s w w s w s w s w w w w w w s w w w w
w s w s w s w s w w w s w w w w w w w s s s s w s w s w s w s s s s w s s s s w
s s s s w s w s w w w s w s s s s s w s w w s w s w s w s s s w w s w w w w s s
s w w w w s w s w w s s w s w w w s w s w w s w s w s w w w w w w s w w w w w s
s s s s w s w s s w w s s s s w w s w s w w s s s s s s s s s s w s s s s s w s
w s w s w w w s w w w s w w s w w s w s w w w w w w w w w w w s w w w w w s s w
w s w s s s s s s s s s s w s s s s w s s s s s s s s s s s s s s s s s w w s G
"""