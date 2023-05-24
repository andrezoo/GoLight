# Example file showing a basic pygame "game loop"
import pygame
import pygame.gfxdraw
# Main atributes
width, heigth = 1280, 720

# pygame setup
pygame.init()
screen = pygame.display.set_mode((width, heigth))
clock = pygame.time.Clock()
running = True
# COLORS
GREY = (228,228,228)
BLUE = (103,155,228)
# lines

pygame.display.set_caption("GoLight 0.1v")

# y=kx+b
def drawLinear(k,b, r):
    pygame.draw.line(screen, BLUE, [r[0], k*r[0]+b], [r[1], k*r[1]+b]) 

# x=b, vertical line
def drawVertical(x, r):
    pygame.draw.line(screen, BLUE, [x, r[0]], [x, r[1]]) 

# Rectangular Prism
def makeRectPrism(a, b, c):
    pygame.gfxdraw.filled_polygon(screen, (a,b,c), BLUE)

screen.fill("white")
lpos = [-1,-1]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            lpos=event.pos # set the last position of cursor
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)

    # fill the screen with a color to wipe away anything from last frame
    
    # RENDER YOUR GAME HERE
    # background mesh

    # сетка
    for x in range(0, width, 40):
        pygame.draw.line(screen, GREY, [x, 0], [x, heigth])
    for y in range(0, heigth, 40):
        pygame.draw.line(screen, GREY, [0, y], [width, y])

    # прицел
    if pygame.mouse.get_focused():
        drawVertical(lpos[0],[0,heigth])
        drawLinear(0, lpos[1], [0,width])

    makeRectPrism((120,120),(120,240),(240,240))

    # flip() the display to put your work on screen
    pygame.display.flip()
    screen.fill("white")

    clock.tick(120)  # limits FPS to 60

pygame.quit()