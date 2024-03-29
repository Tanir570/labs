import pygame
pygame.init()

x = 250
y = 250
screen = pygame.display.set_mode((500, 500))
speed = 20
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= speed
            elif event.key == pygame.K_DOWN:
                y += speed
            elif event.key == pygame.K_RIGHT:
                x += speed
            elif event.key == pygame.K_LEFT:
                x -= speed

    x = max(25, min(x, 500 - 25))
    y = max(25, min(y, 500 - 25))

    screen.fill('white')
    pygame.draw.circle(screen, "red", (x, y), 25)
    pygame.display.update()

pygame.quit()
