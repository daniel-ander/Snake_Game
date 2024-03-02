# Steps for the game:
"""
1 Create the blank window and the game loop
2 create the different objects in the game world
3 move the snake
4 make the snake eat the food
5 make the snake grow longer
6 check for collision with the edges and the tail of the snake
7 add title and frame
8 keep the score
9 add sounds if u want
"""


import pygame
import sys
from pygame.math import Vector2
import random

pygame.init()

GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

cell_size = 30
number_of_cells = 25
    # this class creates the food using a Vector2 object 
class Food:
    def __init__(self):
        self.position = self.generate_random_pos()
    
    # this creates an invisible rectangle around the food, it puts it at the coords of the food * the cell size
    # and then it draws a rectangle on the screen with the color dark green
    def draw(self):
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        #below isnt used anylonger since we use an image for the food
        #pygame.draw.rect(screen, DARK_GREEN, food_rect)
        screen.blit(food_surface, food_rect)

    # this creates a random position for the food using the number of cells -1, returning it as a Vector2 object
    def generate_random_pos(self):
        x = random.randint(0, number_of_cells -1)
        y = random.randint(0, number_of_cells -1)
        position = Vector2(x,y)
        return position

class Snake: 
    def __init__(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        # this is the direction the snake will move, (1,0) is right, (-1,0) is left, (0,1) is down, (0,-1) is up
        self.direction = Vector2(1, 0)

    def draw(self):
        for segment in self.body:
            segment_rect = (segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, DARK_GREEN, segment_rect, 0,)
    
    def update(self):
        # selects all elements up to the second to last element in the list, reassigned to itself without last element
        self.body = self.body[:-1]
        # inserts a new element to the start of the list, takes first element in list and adds the (x,y) direction to it
        self.body.insert(0, self.body[0] + self.direction)


screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))

pygame.display.set_caption("Retro Snake")

clock = pygame.time.Clock()

food = Food()
snake = Snake()
food_surface = pygame.image.load("Graphics/food.png")


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    snake.update()
    
    # draws background for screen
    screen.fill(GREEN)

    # draws the food
    food.draw()
    # draws the snake
    snake.draw()
    pygame.display.update()
    clock.tick(60)

