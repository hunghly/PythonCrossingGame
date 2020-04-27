# Gain access to the pygame library
import pygame

# screen data
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy RPG'
# Color according to RGB code
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
# Clock used to update game events and frames
clock = pygame.time.Clock()


class Game:
    # typical rate of 60, or 60 FPS
    TICK_RATE = 60

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        # Create the window of specified size in width to display the game
        game_screen = pygame.display.set_mode((width, height))
        # Set the game window color to white
        game_screen.fill(WHITE_COLOR)
        # change title
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False
        # Runs until is_game_over = True
        while not is_game_over:

            # a loop to get all of the events occuring at any given time
            # events are most often mouse movement, mouse and button clicks, or exit events
            for event in pygame.event.get():
                # if we have a quit type event then exit out of loop
                if event.type == pygame.QUIT:
                    is_game_over = True
                print(event)

            # update all game graphics
            pygame.display.update()
            # tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)


class GameObject:

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        # scale up the image and assign to image field
        self.image = pygame.transform.scale(object_image, (width, height))
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))


class PlayerCharacter(GameObject):

    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)


pygame.init()
# Create a new game instance
new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

pygame.quit()
quit()

# pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
# pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)
# game_screen.blit(player_image, (375, 375))


# main game loop used to update all game play such as movement, checks, and graphics
