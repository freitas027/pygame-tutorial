
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

pygame.init()

#Set screen size
size = (1000, 1000)
screen = pygame.display.set_mode(size)

# Middle of the screen, will be used later
mid = (size[0]/2, size[1]/2)

# Initialize some variables and fill screen with white
clock = pygame.time.Clock()
pygame.display.set_caption("Drawing a sprial with a constant linear velocity")
done = False
t0 = time.time()
screen.fill(WHITE)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    t = time.time() - t0
    v = 1000
    # A spiral can be defined as r=th in the polar coordinates
    # Using a polar->cartesian transformation, x=r*cos(th), y=r*sin(th)
    #                                          x=th*cost(th), y=th*sin(th) (for a sprial)
    # th = w*t (1)
    # linear velocity: v=w*r
    #                  w=v/r -> (for a sprial) w=v/th (2)
    # Substituting (2) -> (1)
    # th = v/th*t
    # th**2 =v*t 
    # th = sqrt(v*t)
    th = math.sqrt(v*2*t)
    x = mid[0]+ th*math.cos(th)
    y = mid[1]+ th*math.sin(th)
    
    pygame.draw.circle(screen, GREEN, (int(x),int(y)), 1)
    pygame.display.flip()
    clock.tick(120)

pygame.quit()