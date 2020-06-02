from game import Game
import pygame
from image_actor import ImageActor
import math
from scene import Scene
from shell import Shell
from block import Block
from level_loader import LevelLoader
from life_bar import LifeBar
from tank import Tank


life1 = LifeBar(5, 2, (0,100,0))
life2 = LifeBar(1095, 2, (255,0,0))
tank1 = Tank(
    'kub3.png',
    0, 800,
    {'u': pygame.K_w,
     'd': pygame.K_s,
     'l': pygame.K_a,
     'r': pygame.K_d
     }, 0, life1)
tank2 = Tank(
    'kub4.png',
    1200, 800,
    {'u': pygame.K_UP,
     'd': pygame.K_DOWN,
     'l': pygame.K_LEFT,
     'r': pygame.K_RIGHT}, 1, life2)
scene = Scene()
game_ui = Scene()

world = Scene()
LevelLoader('map_daniil.txt', world)
world.add_actor(tank1)
world.add_actor(tank2)

game_ui.add_actor(life1)
game_ui.add_actor(life2)

scene.add_actor(world)
scene.add_actor(game_ui)

game = Game(scene, 1200, 800)
game.run()
