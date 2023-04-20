import pygame
import os.path

from interface import Interface
from wave_generator import DataPlotter
from button import Button, ButtonManager

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
        self.text_input_box_px = 40
        self.text_input_box_py = 40
        self.text_input_box = pygame.Rect((self.display.get_width() - self.text_input_box_width) // 2,
                                           (self.display.get_height() - self.text_input_box_height) // 6,
                                           self.text_input_box_width,
                                           self.text_input_box_height)
        
        self.text_input = ""
        self.dataplt = DataPlotter()
        self.image_path = os.path.join('./generated_waves/plot.png')

        # load image
        self.current_image = None
        try:
            self.current_image = pygame.image.load(self.image_path)
        except:
            pass

        # buttons
        self.button_manager = ButtonManager()
        self.button_manager.add_button(100, 100, 50, 50, (50, 50, 50), "Button", 12, (0, 0, 0))
        

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
                    self.text_input_box.top = self.display.get_height() // 6

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print(self.text_input)
                        self.dataplt.plot(self.text_input)
                        self.text_input = ""
                        self.current_image = pygame.image.load(self.image_path)
                    elif event.key == pygame.K_BACKSPACE:
                        self.text_input = self.text_input[:-1]
                    else:
                        self.text_input += event.unicode

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    button = self.button_manager.get_clicked(mouse_pos)
                    if button is not None:
                        print(f"Button '{button.text}' clicked!")

            self.display.fill(self.background_color) # background
            pygame.draw.rect(self.display, (0, 0, 0), self.text_input_box, 2) # text box
            text_surface = self.font.render(self.text_input, True, (0, 0, 0)) # text that's being written
            text_rect = text_surface.get_rect(center=self.text_input_box.center) # text that's being written
            self.display.blit(text_surface, text_rect) # text that's being written

            # display image
            if self.current_image is not None:
                try:
                    image_rect = self.current_image.get_rect()
                    image_pos = ((self.display.get_width() - image_rect.width) // 2, (self.display.get_height() - image_rect.height) // 2 + self.display.get_height() // 6)
                    self.display.blit(self.current_image, image_pos)

                except pygame.error as e:
                    print(f'Error displaying image: {e}')

            # draw buttons
            for button in self.button_manager.buttons:
                button.draw(self.display)


            # update display
            pygame.display.update()

