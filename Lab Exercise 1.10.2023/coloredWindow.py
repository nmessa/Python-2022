import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([100, 150, 200])
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
