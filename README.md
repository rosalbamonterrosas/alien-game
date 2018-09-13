Alien Game

In this alien game, which uses Pygame, the player controls a ship that appears at the bottom center of the screen. The player can move the ship right and left using arrow keys. The bullets that will come out of the ship also has been created.

The file alien_invasion.py contains the main loop for the program, and initializes pygame, settings, screen object, and the ship. 

The file settngs.py contains a Settings class that stores all the settings for the game. The screen, ship, and bullet settings have already been initialized in this class. 

The file ship.py contains the class Ship, which loads the ship's image and sets its position at the bottom center of the screen. As the player presses the right and left arrow keys, the ship's position gets updated. 

The file game_functions.py checks for certain events, such as if the user has pressed the right or left arrow keys, or if the user quits the game. The screen is also updated.

The file bullet.py contains the class Bullet, which inherits from the Sprite class in the pygame.sprite module, manages the bullets fired from the ship. The bullet, which is not based on an image, is built from scratch using the pygame.Rect() class.

To Be Developed:
The player shoots bullets using the spacebar. When the game begins, a fleet of aliens fill the sky and moves across and down the screen. The player shoots and destroys the aliens. If the player shoots all the aliens, a new fleet appears that moves faster than the previous fleet. If any alien hits the player's ship or reaches the bottom of the screen, the player loses a ship. The player will given only three ships and if the player loses all three ships, the game ends. A scoreboard will also appear on the screen.
