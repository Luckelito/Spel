import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
done = False

while not done:
    for i in range(6):
        for j in range(3):
            pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(270 * i + 150, 270 * j + 50, 250, 250))

    pressed = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()