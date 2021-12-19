import random
import pygame
import pygame_gui

# initialize the game
pygame.init()

# define RGB values
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen = pygame.display.set_mode((800, 600))

# sets variable for the startscreen
startscreen = pygame.display.set_mode((800, 600))

# sets variable for the background
background = pygame.Surface((800, 600))

# sets the color of the background
background.fill(pygame.Color('#FFFFFF'))

pygame.display.set_caption("pyMon")

# creates font object
font = pygame.font.SysFont('arialunicode', 30)

# create text object
text = font.render('pyMon', True, (0, 0, 0))

manager = pygame_gui.UIManager((800, 600))

play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)), text='Play',
                                           manager=manager)

clock = pygame.time.Clock()

running = True


class PyMon:
    def __init__(self):
        pygame.init()

        self.display_width = 800
        self.display_height = 600
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.gameDisplay = None


while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.USEREVENT:

            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

                if event.ui_element == play_button:
                    running = False

    manager.process_events(event)

    manager.update(time_delta)

    startscreen.blit(background, (0, 0))

    manager.draw_ui(startscreen)

    startscreen.blit(text, (0, 0))

    pygame.display.update()

# Game mechanics

# user_input = input("Select a choice (Charmander, Squirtle, or Bulbasaur): ")

# options = ["Charmander", "Squirtle", "Bulbasaur"]

# computer_input = random.choice(options)

# if user_input == computer_input:
# print("It's a Tie! Try Again.")
# else:
# if user_input == "Charmander" and computer_input == "Bulbasaur":
# print("The Computer Picked Bulbasaur, You Win!")

# if user_input == "Squirtle" and computer_input == "Charmander":
# print("The Computer Picked Charmander, You Win!")

# if user_input == "Bulbasaur" and computer_input == "Squirtle":
# print("The Computer Picked Squirtle, You Win!")


# if user_input == "Charmander" and computer_input == "Squirtle":
# print("The Computer Picked Squirtle, You Lose!")

# if user_input == "Squirtle" and computer_input == "Bulbasaur":
# print("The Computer Picked Bulbasaur, You Lose!")

# if user_input == "Bulbasaur" and computer_input == "Charmander":
# print("The Computer Picked Charmander, You Lose!")
