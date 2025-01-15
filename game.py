"""# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Screen dimensions
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Scrolling Shooter Game")

# # Colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)

# # Load images
# player_image = pygame.Surface((50, 50))  # Placeholder for spaceship image
# player_image.fill(WHITE)

# bullet_image = pygame.Surface((5, 10))  # Placeholder for bullet image
# bullet_image.fill(WHITE)

# enemy_image = pygame.Surface((50, 50))  # Placeholder for enemy image
# enemy_image.fill((255, 0, 0))

# # Player class
# class Player:
#     def __init__(self):
#         self.image = player_image
#         self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))
#         self.speed = 5

#     def move(self, dx):
#         self.rect.x += dx
#         # Keep player on the screen
#         self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))

#     def draw(self, surface):
#         surface.blit(self.image, self.rect)

# # Bullet class
# class Bullet:
#     def __init__(self, x, y):
#         self.image = bullet_image
#         self.rect = self.image.get_rect(center=(x, y))
#         self.speed = -10

#     def update(self):
#         self.rect.y += self.speed

#     def draw(self, surface):
#         surface.blit(self.image, self.rect)

# # Enemy class
# class Enemy:
#     def __init__(self):
#         self.image = enemy_image
#         self.rect = self.image.get_rect(x=random.randint(0, WIDTH - 50), y=0)
#         self.speed = 3

#     def update(self):
#         self.rect.y += self.speed

#     def draw(self, surface):
#         surface.blit(self.image, self.rect)

# # Game loop
# def main():
#     clock = pygame.time.Clock()
#     player = Player()
#     bullets = []
#     enemies = []
#     score = 0

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             player.move(-player.speed)
#         if keys[pygame.K_RIGHT]:
#             player.move(player.speed)
#         if keys[pygame.K_SPACE]:
#             bullets.append(Bullet(player.rect.centerx, player.rect.top))

#         # Update bullets
#         for bullet in bullets[:]:
#             bullet.update()
#             if bullet.rect.bottom < 0:
#                 bullets.remove(bullet)

#         # Create enemies
#         if random.randint(1, 30) == 1:  # Randomly spawn an enemy
#             enemies.append(Enemy())

#         # Update enemies
#         for enemy in enemies[:]:
#             enemy.update()
#             if enemy.rect.top > HEIGHT:
#                 enemies.remove(enemy)
#                 score += 1  # Increase score when an enemy goes off-screen

#         # Draw everything
#         screen.fill(BLACK)
#         player.draw(screen)
#         for bullet in bullets:
#             bullet.draw(screen)
#         for enemy in enemies:
#             enemy.draw(screen)

#         # Display score
#         font = pygame.font.Font(None, 36)
#         text = font.render(f"Score: {score}", True, WHITE)
#         screen.blit(text, (10, 10))

#         pygame.display.flip()
#         clock.tick(60)

#     pygame.quit()

# if __name__ == "__main__":
#     main()


# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Constants
# WIDTH, HEIGHT = 800, 600
# FPS = 60
# GRAVITY = 0.5

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)

# # Set up the display
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Simple Platformer")

# # Player class
# class Player:
#     def __init__(self):
#         self.rect = pygame.Rect(100, HEIGHT - 150, 50, 50)
#         self.speed_y = 0
#         self.on_ground = False

#     def update(self):
#         self.speed_y += GRAVITY
#         self.rect.y += self.speed_y

#         if self.rect.y >= HEIGHT - 50:
#             self.rect.y = HEIGHT - 50
#             self.on_ground = True
#             self.speed_y = 0
#         else:
#             self.on_ground = False

#     def jump(self):
#         if self.on_ground:
#             self.speed_y = -15

# # Main function
# def main():
#     clock = pygame.time.Clock()
#     player = Player()

#     # Game loop
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     player.jump()

#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             player.rect.x -= 5
#         if keys[pygame.K_RIGHT]:
#             player.rect.x += 5

#         player.update()

#         # Fill the screen
#         screen.fill(WHITE)
#         pygame.draw.rect(screen, GREEN, player.rect)

#         # Refresh the display
#         pygame.display.flip()
#         clock.tick(FPS)

# if __name__ == "__main__":
#     main()













Snake Eater
Made with PyGame


import pygame, sys, time, random


# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
difficulty = 25

# Window size
frame_size_x = 720
frame_size_y = 480

# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')


# Initialise game window
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


# FPS (frames per second) controller
fps_controller = pygame.time.Clock()


# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0


# Game Over
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()


# Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Making sure the snake cannot move in the opposite direction instantaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawning food on the screen
    if not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
    food_spawn = True

    # GFX
    game_window.fill(black)
    for pos in snake_body:
        # Snake body
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Snake food
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    # Getting out of bounds
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
        game_over()
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    show_score(1, white, 'consolas', 20)
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    fps_controller.tick(difficulty)"""







# import random 
# son = (random.randrange(0,10))
# savol = int(input("ixtiyoriy son kiriting: "))
# if son == savol:
#     print(f"tabriklayman siz topdingiz 👍👏")
# elif son != savol:
#     print("Siz topa olmadingiz, battar boling 😆")





