import pygame
from interface import Interface

class app:
    def __init__(self):
        pygame.init()

        self.min_display_size = (Interface.MINIMUM_WIDTH, Interface.MINIMUM_HEIGHT)

        # resizable display
        self.display = pygame.display.set_mode(self.min_display_size, pygame.RESIZABLE)

        # back ground color to white
        self.background_color = (255, 255, 255)

        # font configuration
        self.font = pygame.font.Font(None, 24)

        # text input box
        self.text_input_box_width = 200
        self.text_input_box_height = 40
        self.text_input_box = pygame.Rect((self.display.get_width() - self.text_input_box_width) // 2,
                                           (self.display.get_height() - self.text_input_box_height) // 2,
                                           self.text_input_box_width,
                                           self.text_input_box_height)
        self.text_input = ""

    def run(self):
        while True:
            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.VIDEORESIZE:
                    # resize the display surface
                    self.display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    # update the text input box position
                    self.text_input_box.left = (self.display.get_width() - self.text_input_box_width) // 2
                    self.text_input_box.top = (self.display.get_height() - self.text_input_box_height) // 2

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print(self.text_input)
                        self.text_input = ""
                    elif event.key == pygame.K_BACKSPACE:
                        self.text_input = self.text_input[:-1]
                    else:
                        self.text_input += event.unicode

            self.display.fill(self.background_color) # background
            pygame.draw.rect(self.display, (0, 0, 0), self.text_input_box, 2) # text box
            text_surface = self.font.render(self.text_input, True, (0, 0, 0)) # text thats being writen
            text_rect = text_surface.get_rect(center=self.text_input_box.center) # text thats being writen
            self.display.blit(text_surface, text_rect) # text thats being writen

            # update display
            pygame.display.update()

