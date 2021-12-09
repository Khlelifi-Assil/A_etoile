import pygame
import numpy as np
import heuristique_script

#Constantes
#Matrice Size
N = 13
#Matrice Gride
grid = np.random.randint(2, size=(N, N))
print(grid)
# starting position
start = [0, 0]
# ending position
end = [6, 5]
# cost per movement
cost = 1
#Window size
WINDOW_SIZE = [290, 290]
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (127, 127, 127)
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 2

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[start[0]][start[1]] = 1

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen

screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
path = heuristique_script.heuristique(grid, cost, start, end)
path_matrice = np.asmatrix(path)
print(path_matrice)

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        
 
    # Set the screen background
    screen.fill(BLACK)
    # Draw the grid
    for row in range(N):
        for column in range(N):
            color = WHITE
            if grid[row][column] == 1:
                color = BLACK
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    if path_matrice.any() != None:
        for rows in range(N):
         for columns in range(N):
            color = WHITE
            if path_matrice[rows,columns] > 1:
                color = GRAY
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * columns + MARGIN,
                              (MARGIN + HEIGHT) * rows + MARGIN,
                              WIDTH,
                              HEIGHT])
    
    color = GREEN
    pygame.draw.rect(screen, color,
                 [(MARGIN + WIDTH) * start[0] + MARGIN,
                  (MARGIN + HEIGHT) * start[1] + MARGIN, WIDTH, HEIGHT])
    color = RED
    pygame.draw.rect(screen, color,
                 [(MARGIN + WIDTH) * end[0] + MARGIN,
                  (MARGIN + HEIGHT) * end[1] + MARGIN, WIDTH, HEIGHT])                          
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.

pygame.quit()
