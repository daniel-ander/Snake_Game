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

title_font = pygame.font.Font(None, 60)
score_font = pygame.font.Font(None, 40)

GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

cell_size = 30
number_of_cells = 25

OFFSET = 50
    # this class creates the food using a Vector2 object 
class Food:
    def __init__(self, snake_body):
        self.position = self.generate_random_pos(snake_body)
    
    # this creates an invisible rectangle around the food, it puts it at the coords of the food * the cell size
    # and then it draws a rectangle on the screen with the color dark green
    def draw(self):
        food_rect = pygame.Rect(OFFSET + self.position.x * cell_size, OFFSET + self.position.y * cell_size, cell_size, cell_size)
        #below isnt used anylonger since we use an image for the food
        #pygame.draw.rect(screen, DARK_GREEN, food_rect)
        screen.blit(food_surface, food_rect)

    def generate_random_cell(self):
        x = random.randint(0, number_of_cells -1)
        y = random.randint(0, number_of_cells -1)
        return Vector2(x,y)

    # this creates a random position for the food using the number of cells -1, returning it as a Vector2 object
    def generate_random_pos(self, snake_body):
        position = self.generate_random_cell()
        while position in snake_body:
            position = self.generate_random_cell()
        return position

class Snake: 
    def __init__(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        # this is the direction the snake will move, (1,0) is right, (-1,0) is left, (0,1) is down, (0,-1) is up
        self.direction = Vector2(1, 0)
        self.add_segment = False
        self.eat_sound= pygame.mixer.Sound("Sounds/Sounds_eat.mp3")
        self.wall_hit_sound = pygame.mixer.Sound("Sounds/Sounds_wall.mp3")

    def draw(self):
        for segment in self.body:
            segment_rect = (OFFSET + segment.x * cell_size, OFFSET + segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, DARK_GREEN, segment_rect, 0,7)
    
    def update(self):
        # inserts a new element to the start of the list, takes first element in list and adds the (x,y) direction to it
        self.body.insert(0, self.body[0] + self.direction)
        if self.add_segment == True: 
            self.add_segment = False
        else: 
            # selects all elements up to the second to last element in the list, reassigned to itself without last element
            self.body = self.body[:-1]
    
    def reset(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1, 0)
            
            

class Game: # this class initiates the game and creates the snake and food objects
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.state = "RUNNING"
        self.score = 0

    def draw(self):
        self.food.draw()
        self.snake.draw()

    def update(self):
        if self.state == "RUNNING":
            self.snake.update()
            self.check_collision_with_food()
            self.check_collision_with_edges()
            self.check_collision_with_tail()

    def check_collision_with_food(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.generate_random_pos(self.snake.body)
            self.snake.add_segment = True
            self.score += 1
            self.snake.eat_sound.play()

    def check_collision_with_edges(self):
        if self.snake.body[0].x == number_of_cells or self.snake.body[0].x == -1:
            self.game_over()

        if self.snake.body[0].y == number_of_cells or self.snake.body[0].y == -1:
            self.game_over()
    def check_collision_with_tail(self):
        headless_snake = self.snake.body[1:]
        if self.snake.body[0] in headless_snake:
            self.game_over()

    def game_over(self):
        self.snake.reset()
        self.food.position = self.food.generate_random_pos(self.snake.body)
        self.state = "STOPPED"
        self.score = 0
        self.snake.wall_hit_sound.play()





screen = pygame.display.set_mode((2*OFFSET + cell_size * number_of_cells, 2*OFFSET + cell_size * number_of_cells))

pygame.display.set_caption("Retro Snake")

clock = pygame.time.Clock()
game = Game()

food_surface = pygame.image.load("Graphics/food.png")

# this declares a variable for a new event that will fire every 200ms
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)


while True: 
    for event in pygame.event.get():
        # this checks if the event is an update user event from the timer
        if event.type == SNAKE_UPDATE:
            game.update()

        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # this impliments movement if a key is pressed down. it wont allow you to go left if youre going right, etc
        if event.type == pygame.KEYDOWN:
            if game.state == "STOPPED":
                game.state = "RUNNING"

            if event.key == pygame.K_UP and game.snake.direction != Vector2(0,1):
                game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and game.snake.direction != Vector2(0,-1):
                game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT and game.snake.direction != Vector2(1, 0):
                game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1, 0):
                game.snake.direction = Vector2(1,0)

    # draws background for screen
    screen.fill(GREEN)
    pygame.draw.rect(screen, DARK_GREEN, (
        OFFSET-5, OFFSET-5, cell_size*number_of_cells+10, cell_size*number_of_cells+10), 5)
    game.draw()
    title_surface = title_font.render("Snake Retro", True, DARK_GREEN)
    # blit stands for block image transfer, it transfers the title_surface to the screen
    score_surface = score_font.render("Score: " + str(game.score), True, DARK_GREEN)
    screen.blit(title_surface, (OFFSET-5, 10))
    screen.blit(score_surface, (OFFSET-5, OFFSET + cell_size * number_of_cells +10))
    pygame.display.update()
    clock.tick(60)

