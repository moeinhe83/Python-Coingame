# Making A Coin Collecting Game With Python

# Library
import pygame
import random

# Init Pygame
pygame.init()

# Display
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Coin Collecting Game')

# Color For Game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
dark_gray = (40, 40, 40)
light_gray = (120, 120, 120)

# Player Setting
player_width = 30
player_height = 30
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 10

# Barrier Setting
obstacle_width = 100
obstacle_height = 20
obstacle_x = random.randint(0, screen_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 3
obstacle_speed_increase = 0.2

# Coin Setting
coin_radius = 15
coin_x = random.randint(coin_radius, screen_width - coin_radius)
coin_y = -coin_radius
coin_speed = 4
coin_speed_increase = 0.2

# Value
clock = pygame.time.Clock()  # Framerate Game
score = 0
normal_font = pygame.font.Font(None, 40)
game_over_font = pygame.font.Font(None, 80)
dark_mode = True
running = True  # Stop Or Pause Game
game_over = False  # For Game Over

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                player_x = screen_width // 2 - player_width // 2
                player_y = screen_height - player_height - 10
                obstacle_x = random.randint(0, screen_width - obstacle_width)
                obstacle_y = -obstacle_height
                obstacle_speed = 3
                coin_x = random.randint(
                    coin_radius, screen_width - coin_radius)
                coin_y = -coin_radius
                coin_speed = 4
                score = 0

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed

        elif keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed

        # An obstacle somewhere
        obstacle_y += obstacle_speed
        if obstacle_y > screen_height:
            obstacle_x = random.randint(0, screen_width - obstacle_width)
            obstacle_y = -obstacle_height
            obstacle_speed += obstacle_speed_increase

        # Coin everywhere
        coin_y += coin_speed
        if coin_y > screen_height:
            coin_x = random.randint(coin_radius, screen_width - coin_radius)
            coin_y = -coin_radius
            coin_speed += coin_speed_increase

        if player_x < obstacle_x + obstacle_width and player_x + player_width > obstacle_x and player_y < obstacle_y + obstacle_height and player_y + player_height > obstacle_y:
            game_over = True

        if player_x < coin_x + coin_radius and player_x + player_width > coin_x - coin_radius and player_y < coin_y + coin_radius and player_y + player_height > coin_y - coin_radius:
            score += 1
            coin_x = random.randint(coin_radius, screen_width - coin_radius)
            coin_y = -coin_radius

    if dark_mode:
        screen.fill('white')
    else:
        screen.fill('white')

    if game_over:
        game_over_text = game_over_font.render('Game Over', True, red)
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() //
                    2, screen_height // 2 - game_over_text.get_height() // 2))

        restart_text = normal_font.render(
            'Please Press Enter To Play Again', True, red)
        screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() //
                    2, screen_height // 2 - restart_text.get_height() // 2 + 50))

        score_text = normal_font.render(f'Your Score: {score}', True, black)
        screen.blit(score_text, (screen_width // 2 - score_text.get_width() //
                    2, screen_height // 2 - score_text.get_height() // 2 + 100))

    else:
        pygame.draw.rect(screen, yellow, (player_x, player_y,
                         player_width, player_height))
        pygame.draw.rect(screen, red, (obstacle_x, obstacle_y,
                         obstacle_width, obstacle_height))
        pygame.draw.circle(screen, black, (coin_x, coin_y), coin_radius)

        score_text = normal_font.render(f'Your Score: {score}', True, black)
        screen.blit(score_text, (10, 10))

    pygame.display.update()  # Update Display Information
    clock.tick(60)  # Set Framerate => 60

# Quit Game
pygame.quit()

# Finish
# Create By Moein Heshmati
