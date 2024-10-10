# Vampire Survivor-Inspired Game

This game is inspired by the popular title *Vampire Survivors* and is developed using Python and Pygame. Players navigate a dynamic environment, fighting off waves of enemies while upgrading their abilities. This project is based on the YouTube tutorial series **Master Python by Making 5 Games [The New Ultimate Introduction to Pygame]**.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Game Controls](#game-controls)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [License](#license)

## Features
- **Intuitive Gameplay**: Engage in fast-paced action while shooting enemies and dodging attacks.
- **Dynamic Enemy AI**: Enemies chase and attack the player, providing a challenging experience.
- **Bullet Mechanics**: Players can shoot bullets with cooldowns and collision detection.
- **Player Movement**: Smooth movement and animations for the player character.
- **Sound Effects and Music**: Enjoy immersive audio, including background music and sound effects.
- **Level Design**: Levels designed using Tiled Map Editor with collision detection.

## Game Controls
- W: Move Up
- S: Move Down
- A: Move Left
- D: Move Right
- Left Mouse Button: Shoot


## File Descriptions
- main.py: The main game loop that initializes Pygame, handles events, updates game objects, and renders graphics.
- player.py: Defines the Player class, which manages player movement, input, animation, and collision detection.
- sprites.py: Contains definitions for various sprite classes, including Bullet, Enemy, Gun, and CollisionSprite, which handle their respective behaviors and animations.
- settings.py: Contains game settings, including window dimensions and tile size.
- data/maps/world.tmx: The Tiled map file that defines the game level layout.
- images/: Directory containing images for the player, enemies, and projectiles.
- audio/: Directory containing sound effects and music used in the game.

## Acknowledgments
- This project is based on the YouTube tutorial series "Master Python by Making 5 Games [The New Ultimate Introduction to Pygame]".
  A special thanks to the creator for providing valuable resources and guidance.
- Special thanks to the Pygame community for their resources and support.
- Game assets (images, sounds) used in the project are sourced from various free resources.
