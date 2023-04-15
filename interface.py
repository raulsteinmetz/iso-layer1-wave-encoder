class Interface:
    MINIMUM_WIDTH = 400
    MINIMUM_HEIGHT = 300
    def get_position(px, py, screenw, screenh):
        return ((px/100) * screenw, (py/100) * screenh)
