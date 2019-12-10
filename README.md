# Alien Attack Game

In this alien game, which uses Pygame, the player controls a ship that appears at the bottom center of the screen. The player can move the ship right and left using the arrow keys. The player can shoot 3 bullets at a time from the ship using the spacebar. To begin the game, the player can click on the play button or press p on the keyboard. The player can quit the game at any time by pressing q on the keyboard or closing the game. 

When the game begins, a fleet of aliens fill the sky and moves across and down the screen. The player shoots bullets and destroys the aliens. If the player shoots down all of the aliens, the player moves up a level, where a new fleet appears that moves faster than the previous fleet, and the ship can also travel faster. Each new level is more difficult than the previous level. If any alien hits the player's ship or reaches the bottom of the screen, the player loses a ship. The player is given only three ships and if the player loses all three ships, the game ends. 

The scoreboard is displayed at the top of the screen, which includes the level number, the number of remaining ships the player has left, the high score, and the current score. When a player quits a game, the high score is saved and displayed again the next time the player starts a new game.

## To play the game, follow the steps below:
* Clone the repo: `git clone https://github.com/rosalbamonterrosas/alien-game.git`
* `cd alien-game`
* Spin up a virtual environment: `python3 -m venv venv/`
* Enter venv: `source venv/bin/activate`
* Install pygame: `pip3 install pygame`
* Run the game: `python3 alien_attack.py`
