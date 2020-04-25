# Gain access to the pygame library
import pygame

pygame.init();
print('hello')

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy RPG'
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()
TICK_RATE = 60
is_game_over = False

# Create the window of specified size in width to display the game
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Set the game window color to white
game_screen.fill(WHITE_COLOR)
# change title
pygame.display.set_caption(SCREEN_TITLE)

# main game loop used to update all game play such as movement, checks, and graphics
#Runs until is_game_over = True
while not is_game_over:

    # a loop to get all of the events occuring at any given time
    # events are most often mouse movement, mouse and button clicks, or exit events
    for event in pygame.event.get():
        # if we have a quit type event then exit out of loop
        if event.type == pygame.QUIT:
            is_game_over = True
        print(event)

    pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
    pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

    # update all game graphics
    pygame.display.update()
    # tick the clock to update everything within the game
    clock.tick(TICK_RATE)


pygame.quit()
quit()