import pygame
import os.path

from interface import Interface
from wave_generator import DataPlotter
from button import Button, ButtonManager
import description

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
        self.font2 = pygame.font.Font(None, 20)

        # text input box
        self.text_input_box_width = 400
        self.text_input_box_height = 40
        self.text_input_box = pygame.Rect((self.display.get_width() - self.text_input_box_width) // 3,
                                           (self.text_input_box_height) * 4.5,
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

        # rectangle
        self.info_rectangle_width = 750
        self.info_rectangle_height = 75
        self.info_rectangle = pygame.Rect((self.display.get_width() - self.text_input_box_width) // 10,
                                           (self.text_input_box_height),
                                           self.info_rectangle_width,
                                           self.info_rectangle_height)
        
        self.current_info = ''
        self.current_encode = 'NRZ-L'



        # buttons
        self.button_manager = ButtonManager(Interface.MINIMUM_WIDTH, Interface.MINIMUM_HEIGHT)
        self.button_manager.add_button(85, 30, Interface.BUTTON_WIDTH, Interface.BUTTON_HEIGHT, (50, 50, 50), "NRZ-I", 12, (255, 255, 255))
        self.button_manager.add_button(85, 45, Interface.BUTTON_WIDTH, Interface.BUTTON_HEIGHT, (50, 50, 50), "NRZ-L", 12, (255, 255, 255))
        self.button_manager.add_button(85, 60, Interface.BUTTON_WIDTH, Interface.BUTTON_HEIGHT, (50, 50, 50), "AMI", 12, (255, 255, 255))
        self.button_manager.add_button(85, 75, Interface.BUTTON_WIDTH, Interface.BUTTON_HEIGHT, (50, 50, 50), "PSEUDOTERNARIO", 12, (255, 255, 255))
        self.button_manager.add_button(70, 30, Interface.BUTTON_WIDTH, Interface.BUTTON_HEIGHT, (50, 50, 50), "MANCHESTER", 12, (255, 255, 255))
        self.button_manager.add_button(70, 45, Interface.BUTTON_WIDTH, Interface.BUTTON_HEIGHT, (50, 50, 50), "MANCHESTER DIFERENCIAL", 12, (255, 255, 255))
        self.button_manager.add_button(70, 60, Interface.BUTTON_WIDTH, Interface.BUTTON_HEIGHT, (50, 50, 50), "MLT-3", 12, (255, 255, 255))
        self.button_manager.add_button(70, 75, Interface.BUTTON_WIDTH, Interface.BUTTON_HEIGHT, (50, 50, 50), "EXTRA 2", 12, (255, 255, 255))
    



    def run(self):
        while True:
            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.dataplt.plot(self.text_input, self.current_encode)
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
                        self.button_manager.button_handler(button, self)

                        
            # text input
            self.display.fill(self.background_color) # background
            pygame.draw.rect(self.display, (0, 0, 0), self.text_input_box, 2) # text box
            text_surface = self.font.render(self.text_input, True, (0, 0, 0)) # text that's being written
            text_rect = text_surface.get_rect(center=self.text_input_box.center) # text that's being written
            self.display.blit(text_surface, text_rect) # text that's being written

            # render the text surface
            text_surface = self.font.render("Digite sinal:", True, (0, 0, 0))
            left_edge = self.text_input_box.left
            text_pos = (left_edge - text_surface.get_width() - 10, self.text_input_box.top + 10)
            self.display.blit(text_surface, text_pos)

            # display image
            if self.current_image is not None:
                try:
                    image_rect = self.current_image.get_rect()
                    image_pos = ((self.display.get_width() - image_rect.width) // 10, (self.display.get_height() - image_rect.height) // 2 + self.display.get_height() // 8)
                    self.display.blit(self.current_image, image_pos)

                except pygame.error as e:
                    print(f'Error displaying image: {e}')

            # draw buttons
            self.button_manager.draw(self.display)

            # info
            pygame.draw.rect(self.display, (0, 0, 0), self.info_rectangle)
            text_surface = self.font2.render(self.current_info, True, (255, 255, 255), 8) # text that's being written
            text_rect = text_surface.get_rect(center=self.info_rectangle.center) # text that's being written
            self.display.blit(text_surface, text_rect) # text that's being written


            # update display
            pygame.display.update()
