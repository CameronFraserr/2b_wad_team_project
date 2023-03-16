import pygame
import random

# initialize Pygame
pygame.init()

# set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# set up the game clock
CLOCK = pygame.time.Clock()

# set up the game fonts
FONT = pygame.font.SysFont('Arial', 50)

# set up the game colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# set up the paddles
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5

player_paddle = pygame.Rect(50, (WINDOW_HEIGHT / 2) - (PADDLE_HEIGHT / 2), PADDLE_WIDTH, PADDLE_HEIGHT)
computer_paddle = pygame.Rect(WINDOW_WIDTH - 50 - PADDLE_WIDTH, (WINDOW_HEIGHT / 2) - (PADDLE_HEIGHT / 2), PADDLE_WIDTH, PADDLE_HEIGHT)

# set up the ball
BALL_SIZE = 10
BALL_SPEED = 5

ball = pygame.Rect((WINDOW_WIDTH / 2) - (BALL_SIZE / 2), (WINDOW_HEIGHT / 2) - (BALL_SIZE / 2), BALL_SIZE, BALL_SIZE)
ball_speed_x = BALL_SPEED * random.choice((1, -1))
ball_speed_y = BALL_SPEED * random.choice((1, -1))

# set up the score
player_score = 0
computer_score = 0

def draw_score():
    player_score_text = FONT.render(str(player_score), True, WHITE)
    computer_score_text = FONT.render(str(computer_score), True, WHITE)
    player_score_rect = player_score_text.get_rect(center=(WINDOW_WIDTH / 4, 50))
    computer_score_rect = computer_score_text.get_rect(center=(WINDOW_WIDTH * 3 / 4, 50))
    WINDOW.blit(player_score_text, player_score_rect)
    WINDOW.blit(computer_score_text, computer_score_rect)

def draw_paddles():
    pygame.draw.rect(WINDOW, WHITE, player_paddle)
    pygame.draw.rect(WINDOW, WHITE, computer_paddle)

def move_player_paddle(key_pressed):
    if key_pressed[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.move_ip(0, -PADDLE_SPEED)
    if key_pressed[pygame.K_DOWN] and player_paddle.bottom < WINDOW_HEIGHT:
        player_paddle.move_ip(0, PADDLE_SPEED)

def move_computer_paddle():
    if ball.y < computer_paddle.y + (PADDLE_HEIGHT / 2):
        computer_paddle.move_ip(0, -PADDLE_SPEED)
    if ball.y > computer_paddle.y + (PADDLE_HEIGHT / 2):
        computer_paddle.move_ip(0, PADDLE_SPEED)
    if computer_paddle.top < 0:
        computer_paddle.top = 0
    if computer_paddle.bottom > WINDOW_HEIGHT:
        computer_paddle.bottom = WINDOW_HEIGHT

def move_ball():
    global ball_speed_x, ball_speed_y, player_score, computer_score

    ball.move_ip(ball_speed_x, ball_speed_y)

    # check for collision with the walls
    if ball.top < 0 or ball.bottom > WINDOW_HEIGHT:
        ball_speed_y *= -1
    if ball.left < 0:
        computer_score += 1
        reset_ball()
    if ball.right > WINDOW_WIDTH:
        player_score += 1
       
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # move the paddles
    move_player_paddle(pygame.key.get_pressed())
    move_computer_paddle()

    # move the ball
    move_ball()

    # draw the game objects
    WINDOW.fill(BLACK)
    draw_score()
    draw_paddles()
    pygame.draw.rect(WINDOW, WHITE, ball)
    pygame.draw.line(WINDOW, WHITE, (WINDOW_WIDTH / 2, 0), (WINDOW_WIDTH / 2, WINDOW_HEIGHT))
    pygame.display.update()

    # set the game speed
    CLOCK.tick(60)
