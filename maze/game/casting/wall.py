from actor import Actor
class Wall(Actor):

    def __init__(self):
<<<<<<< Updated upstream
        """Handles Wall segments
    """
=======
        pass


    def walls_template(self):

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
>>>>>>> Stashed changes
