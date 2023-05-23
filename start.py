# Example file showing a basic pygame "game loop"
import pygame
# Main atributes
width, heigth = 1280, 720

# pygame setup
pygame.init()
screen = pygame.display.set_mode((width, heigth))
clock = pygame.time.Clock()
running = True
# COLORS
GREY = (228,228,228)
# lines
screen.fill("white")
for x in range(0, width, 40):
    pygame.draw.line(screen, GREY, [x, 0], [x, heigth])
for y in range(0, heigth, 40):
    pygame.draw.line(screen, GREY, [0, y], [width, y])

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()