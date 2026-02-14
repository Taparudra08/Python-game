import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game window
WIDTH, HEIGHT = 600, 400
BLOCK = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nokia Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Snake
snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"

# Food
food = (
    random.randrange(0, WIDTH, BLOCK),
    random.randrange(0, HEIGHT, BLOCK)
)

score = 0
game_over_flag = False

def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, (*block, BLOCK, BLOCK))

def game_over():
    text = font.render("Game Over! Press SPACE to Restart", True, RED)
    screen.blit(text, (WIDTH // 6, HEIGHT // 2))
    pygame.display.update()

# Game loop
while True:
    clock.tick(10)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if not game_over_flag:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

            if event.key == pygame.K_SPACE:
                snake = [(100, 100), (80, 100), (60, 100)]
                direction = "RIGHT"
                score = 0
                food = (
                    random.randrange(0, WIDTH, BLOCK),
                    random.randrange(0, HEIGHT, BLOCK)
                )
                game_over_flag = False

    if not game_over_flag:
        # Move snake
        x, y = snake[0]

        if direction == "UP":
            y -= BLOCK
        elif direction == "DOWN":
            y += BLOCK
        elif direction == "LEFT":
            x -= BLOCK
        elif direction == "RIGHT":
            x += BLOCK

        # 🔁 WRAP AROUND LOGIC
        x = x % WIDTH
        y = y % HEIGHT

        new_head = (x, y)

        # Collision with self
        if new_head in snake:
            game_over_flag = True

        snake.insert(0, new_head)

        # Eat food
        if new_head == food:
            score += 1
            food = (
                random.randrange(0, WIDTH, BLOCK),
                random.randrange(0, HEIGHT, BLOCK)
            )
        else:
            snake.pop()

    # Draw food & snake
    pygame.draw.rect(screen, RED, (*food, BLOCK, BLOCK))
    draw_snake(snake)

    # Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    if game_over_flag:
        game_over()

    pygame.display.update()
