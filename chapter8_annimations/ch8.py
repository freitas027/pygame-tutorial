"""
    This program will create a snow-stacking effect with pygame.
    The snow particles are created randomly but with a normal distribution.
    The mean of the normal distribution is the middle of the screen, and the variance was set to the Width divided by seven,
since over 99.999% of the particles fall inside the screen.
"""

import pygame
import random
import numpy as np

# Initialize the game engine
pygame.init()
 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
 
# Set the height and width of the screen
XSIZE = 400
YSIZE = 400
 
screen = pygame.display.set_mode((XSIZE, YSIZE))
pygame.display.set_caption("Snow Animation")

spaces = np.zeros(shape=(XSIZE, YSIZE), dtype=int) 
clock = pygame.time.Clock()

# draw on screen based on a numpy 2d matrix (1 position in the matrix signals to draw)
def draw_2d_vector(npvector):
    for (y, row) in enumerate(npvector):
        for (x, item) in enumerate(row):
            if item:
                pygame.draw.circle(screen, WHITE, (x,y), 1)

# This function create a fall down effect but also stack the "snow" particles on top of eachother
def convolute_stack(npmatrix):
    xsize, ysize = np.shape(npmatrix)
    # Iterate over the rows
    for row in range(ysize-1, 0, -1):
        or_result = npmatrix[row, :] | npmatrix[row-1, :]
        and_result = npmatrix[row, :] & npmatrix[row-1, :]
        # Bottom row will be 1 if either the current space is 1 or the space above is 1
        npmatrix[row, :] = or_result
        # Top row will be 1 only if the top and bottom row are 1 (stack)
        npmatrix[row-1, :] = and_result

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Clear the screen
    screen.fill(BLACK)
    
    # Fall down and stack
    convolute_stack(spaces)
    # Draw new matrix
    draw_2d_vector(spaces)
    x = int(round(random.gauss(XSIZE/2, XSIZE/7)))
    if x>=0 and x<XSIZE:
        new_row = np.zeros(XSIZE)
        new_row[x] = 1
        spaces[0,:] = new_row
    
    #Update the screen
    pygame.display.flip()
    clock.tick(120)

pygame.quit()