class Interface:
    MINIMUM_WIDTH = 1080
    MINIMUM_HEIGHT = 800
    BUTTON_HEIGHT = 50
    BUTTON_WIDTH = 120
    def get_position(px, py, screenw, screenh):
        return ((px/100) * screenw, (py/100) * screenh)
