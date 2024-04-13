import pygame
import time
import random

pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Dimensions of the game window
dis_width = 600
dis_height = 400

# Create the game window
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game') 

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Define the size of the snake block and speed of the snake
snake_block = 10
snake_speed = 15

# Define font styles and sizes for text
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Functions below
# Display the player's score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# Display the player's level
def Your_level(level):
    value = score_font.render("Your Level: " + str(level), True, yellow)
    dis.blit(value, [0, 40])  # Positioning the level text

# Draw the snake on the screen
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Display messages on the screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Function to generate food
def generate_food():
    return round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0, round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

# Main game loop
def gameLoop(snake_speed):
    game_over = False
    game_close = False

    # Initialize the snake's position and direction
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    # Initialize the snake's body and length
    snake_List = []
    Length_of_snake = 1

    # Initialize the player's level and score
    level = 1
    score = 0

    # Generate the initial position of the food
    foodx, foody = generate_food()
    food_timer = time.time()  # Timestamp for food generation

    # Game loop
    while not game_over:
        while game_close == True:
            # Display the game over message
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # For the game over screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop(snake_speed)

        # For quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Update the snake's position
        x1 += x1_change
        y1 += y1_change

        # Check for border collision
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Check for food collision
        if x1 == foodx and y1 == foody:
            # Increase score and snake length
            score += 1
            Length_of_snake += 1
            # Generate new food position
            foodx, foody = generate_food()
            food_timer = time.time()  # Reset food timer

            # Increase level every 3 foods
            if score % 3 == 0:
                level += 1
                snake_speed += 2

        # Check if food has expired
        if time.time() - food_timer > 5:  # Food disappears after 5 seconds
            foodx, foody = generate_food()
            food_timer = time.time()  # Reset food timer

        # Draw the game elements on the screen
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check for collision with snake body
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Display the snake, score, and level on the screen
        our_snake(snake_block, snake_List)
        Your_score(score)
        Your_level(level)

        pygame.display.update()

        # Adjust game speed based on snake_speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop(snake_speed)