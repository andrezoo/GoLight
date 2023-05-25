# Example file showing a basic pygame "game loop"
import pygame as pg
import pygame.gfxdraw
import colors

# Main atributes
width, heigth = 1280, 720
lpos = [-1,-1]
mouse_function = "nothing"

# Functions
def drawLinear(k,b, r, color=colors.BLUE):
    pg.draw.line(screen, color, [r[0], k*r[0]+b], [r[1], k*r[1]+b]) 
# x=b, vertical line
def drawVertical(x, r, color=colors.BLUE):
    pg.draw.line(screen, color, [x, r[0]], [x, r[1]]) 
# Rectangular Prism
def makeRectPrism(a, b, c, color=colors.BLUE):
    pg.gfxdraw.filled_polygon(screen, (a,b,c), color)
# Dove Prism
def makeDovePrism(a, b, c, d, color=colors.YELLOW):
    pg.gfxdraw.filled_polygon(screen, (a,b,c,d), color)
# Doing grid
def grid(period, width, heigth, color=colors.GREY):
    for x in range(0, width, period):
        pg.draw.line(screen, color, [x, 0], [x, heigth])
    for y in range(0, heigth, period):
        pg.draw.line(screen, color, [0, y], [width, y])
# Def sight
def sight(lpos, width, height):
    if pg.mouse.get_focused():
        drawVertical(lpos[0],[0,height])
        drawLinear(0, lpos[1], [0,width])

# Pygame setup
pg.init()
screen = pg.display.set_mode((width, heigth))
clock = pg.time.Clock()
running = True

# Name and screen fill
pg.display.set_caption("GoLight 0.1v")
screen.fill("white")

grid(40, width, heigth)
pg.draw.rect(screen, colors.RED, (0, 0, 50, 50))
makeRectPrism((10, 10),(10, 40),(40, 40), colors.WHITE)
pg.draw.rect(screen, colors.ORANGE, (50, 0, 50, 50))
makeDovePrism((60, 30),(70,20),(80,20),(90, 30), colors.WHITE)
pg.draw.rect(screen, colors.YELLOW, (100, 0, 50, 50))
pg.draw.line(screen, colors.WHITE, (110, 25), (140, 25), 5)
pg.draw.line(screen, colors.WHITE, (140, 25), (130, 20), 5)
pg.draw.line(screen, colors.WHITE, (140, 25), (130, 30), 5)


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            print(event)
            lpos=event.pos
            if lpos[0] > 0 and lpos[0] <= 50 and lpos[1] > 0 and lpos[1] <= 50:
                mouse_function = "rect_prism"
            elif lpos[0] > 50 and lpos[0] <= 100 and lpos[1] > 0 and lpos[1] <= 50:
                mouse_function = "dove_prism"
            elif lpos[0] > 100 and lpos[0] <= 150 and lpos[1] > 0 and lpos[1] <= 50:
                mouse_function = "light"
            else:
                if mouse_function == "rect_prism":
                    makeRectPrism(lpos, (lpos[0], lpos[1]+120), (lpos[0]+120, lpos[1]+120))
                elif mouse_function == "dove_prism":
                    makeDovePrism((lpos[0]-120, lpos[1]+120), lpos, (lpos[0]+120, lpos[1]), (lpos[0]+240, lpos[1]+120))
                elif mouse_function == "light":
                    pg.draw.line(screen, colors.BLACK, lpos, [0, lpos[1]], 3)
                    pg.draw.line(screen, colors.BLACK, lpos, [width, lpos[1]], 3)
                    pg.draw.line(screen, colors.BLACK, lpos, [lpos[0], 0], 3)
                    pg.draw.line(screen, colors.BLACK, lpos, [lpos[0], heigth], 3)
                
                
            
        if event.type == pg.MOUSEMOTION:
            lpos=event.pos # set the last position of cursor
        if event.type == pg.MOUSEBUTTONUP and not event.type == pg.MOUSEWHEEL:
            pos = pg.mouse.get_pos()
            print(pos)

    # fill the screen with a color to wipe away anything from last frame
    # Interface
    #screen.fill("white")
    

    
    
    # makeRectPrism((120,120),(120,240),(240,240))
    # makeRectPrism([500,500],[500,620],[620,620])
    # makeDovePrism([0,700], [120, 580], [240, 580], [360, 700])
    
    #sight(lpos, width, heigth)

    # flip() the display to put your work on screen
    pg.display.flip()

    # limits FPS to 60
    clock.tick(120)  

pg.quit()




