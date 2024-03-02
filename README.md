# Retro Snake Game

This is a simple implementation of the classic Snake game using Python and Pygame. The game features a retro design with a grid-based movement system. The player controls a snake that grows longer each time it eats food. The game ends when the snake collides with the edge of the game area or with its own tail.

## Game Steps

1. Create the blank window and the game loop
2. Create the different objects in the game world
3. Move the snake
4. Make the snake eat the food
5. Make the snake grow longer
6. Check for collision with the edges and the tail of the snake
7. Add title and frame
8. Keep the score
9. Add sounds if you want

## Classes

### Food

This class creates the food using a Vector2 object. It creates an invisible rectangle around the food, it puts it at the coords of the food * the cell size and then it draws a rectangle on the screen with the color dark green.

### Snake

This class creates the snake. It has a body which is a list of Vector2 objects. The direction attribute determines the direction the snake will move, (1,0) is right, (-1,0) is left, (0,1) is down, (0,-1) is up.

### Game

This class initiates the game and creates the snake and food objects. It also checks for collisions with food, edges and the snake's own tail. It also has a method to change the theme of the game, changing the colors and fonts of the game. It accesses themes.py to cycle through an index of theme names, setting a variable for those themes.

## Running the Game

The game is run in a while loop. It checks for events such as key presses and updates the game state accordingly. It also draws the game objects on the screen.
