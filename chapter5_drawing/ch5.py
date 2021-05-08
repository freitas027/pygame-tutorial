
"""
    The purpose of this program is to incrementaly draw a spiral with a constant linear velocity
    If the sprial was drawn with a constant angular velocity, it would cause the linear velocity to increase over time, which
makes the incremental dots to start skipping (leaving white spaces).
"""
import pygame
import math
import time
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Set screen size, initialize some variables and fill screen with white
size = (700, 500)
mid = (size[0]/2, size[1]/2)
pygame.init()
font = pygame.font.SysFont('Calibri', 25, True, False)
screen  =pygame.display.set_mode(size)
pygame.display.set_caption("A cool game")
done = False
clock = pygame.time.Clock()
t0 = time.time()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    
    # rate in which lines apper per second
    RATE = 20
    lines = int(RATE*(time.time() - t0))
    # radius of the circle
    R = 200

    # each each iteration will draw one line
    for i in range(0, lines):
        th = (i/lines)* 2*math.pi 
        x = mid[0]+ R*math.cos(th)
        y = mid[1]+ R*math.sin(th)
        pygame.draw.line(screen, GREEN, mid, (x,y), 2)

    # updating the text which states the number of lines
    nlines = font.render("Number of lines: {}".format(lines), False, BLACK)
    screen.blit(nlines, (25,25))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()