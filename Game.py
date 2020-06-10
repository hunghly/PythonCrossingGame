# Gain access to the pygame library
# Implement game classes
# Implement enemy character class and bounds checking
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
        self.game_screen = pygame.display.set_mode((width, height))
        # Set the game window color to white
        self.game_screen.fill(WHITE_COLOR)
        # change title
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False
        direction = 0
        player_character = PlayerCharacter('./images/player.png', 375, 700, 50, 50)
        treasure = GameObject('./images/treasure.png', 375, 50, 50, 50)
        enemy_0 = NonPlayerCharacter('./images/enemy.png', 20, 400, 50, 50)
        # enemy_1 = NonPlayerCharacter('./images/enemy.png', 200, 600, 50, 50)

        # Runs until is_game_over = True
        while not is_game_over:
            # a loop to get all of the events occuring at any given time
            # events are most often mouse movement, mouse and button clicks, or exit events
            for event in pygame.event.get():
                # if we have a quit type event then exit out of loop
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0

                # print(event)

            self.game_screen.fill(WHITE_COLOR)
            treasure.draw(self.game_screen)
            # Move player
            player_character.move(direction, self.height)
            player_character.draw(self.game_screen)
            # Move enemy 0
            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            if player_character.detect_collision(enemy_0):
                is_game_over = True
            elif player_character.detect_collision(treasure):
                is_game_over = True
            # Move enemy 1
            # enemy_1.move(self.width)
            # enemy_1.draw(self.game_screen)

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

    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED
        #     bottom of screen
        if self.y_pos >= max_height - self.height:
            self.y_pos = max_height - self.height
        if self.y_pos <= 0:
            self.y_pos = 0

    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False
        return True


class NonPlayerCharacter(GameObject):
    SPEED = 4

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, max_width):
        if self.x_pos <= 0:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 50:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED


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
