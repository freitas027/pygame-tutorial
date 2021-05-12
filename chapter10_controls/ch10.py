"""
    This scripts create a visual effect of "dots" moving in a different direction. Use arrow keys to change direction and velocity.
"""

import pygame
import numpy as np

pygame.init()

XSIZE = 200
YSIZE = 200
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

screen = pygame.display.set_mode((XSIZE, YSIZE))
screen.fill(BLACK)
clock = pygame.time.Clock()
pygame.display.set_caption("Snake Game")

# Function to draw based on index position only if the stored value equals one
def draw_2d_vector(npvector):
    for (y, row) in enumerate(npvector):
        for (x, item) in enumerate(row):
            if item == 1:
                pygame.draw.circle(screen, WHITE, (x,y), 1)

# Roll the 2d array based on X and Y velocity
def move(nparray, vx, vy):
    rolled_x = np.roll(nparray, vx, axis=1)
    return np.roll(rolled_x, vy, axis=0)

vx = 1
vy = 1

# Define lambda functions that will return incremented vx and vy
key_events = {
    pygame.K_UP: lambda: (vx,vy-1),
    pygame.K_DOWN: lambda: (vx,vy+1),
    pygame.K_LEFT: lambda: (vx-1, vy),
    pygame.K_RIGHT: lambda: (vx+1, vy),
}

done = False
# Create dot matrix, higher value will make drawing more sparse
# Dots are drawn only if equal to one
dots = np.random.randint(0,1001, (XSIZE, YSIZE))

while not done:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            # Get the lambda function from the dictionary
            vel_fn = key_events[event.key]
            # Update vx and vy
            vx, vy = vel_fn()
    
    dots = move(dots, vx, vy)
    screen.fill(BLACK)
    draw_2d_vector(dots)
    pygame.display.flip()
    clock.tick(60)

