import pygame

from ai_tank import AITank
from ai_turele import Turele
from game import Game
from level_loader import LevelLoader
from life_bar import LifeBar
from scene import Scene
from tank import Tank

life1 = LifeBar(5, 2, (0,100,0))
life2 = LifeBar(1095, 2, (255,0,0))
life3 = LifeBar(200, 2, (0, 0, 255))
life4 = LifeBar(900, 2, (0, 0, 255))
tank1 = Tank(
    'kub3.png',
    150, 800,
    {'u': pygame.K_w,
     'd': pygame.K_s,
     'l': pygame.K_a,
     'r': pygame.K_d,
     's': pygame.K_q
     }, 0, life1)
tank2 = Tank(
    'kub4.png',
    1050, 800,
    {'u': pygame.K_UP,
     'd': pygame.K_DOWN,
     'l': pygame.K_LEFT,
     'r': pygame.K_RIGHT,
     's': pygame.K_PAGEDOWN}, 1, life2)
ai1  = Turele(
    'kub5.png',
    250, 375, 1, life3)
ai2  = Turele(
    'kub5.png',
    950, 375, 1, life4)
scene = Scene()
game_ui = Scene()


world = Scene()
LevelLoader('map_daniil.txt', world)
world.add_actor(tank1)
world.add_actor(tank2)

world.add_actor(ai1)
world.add_actor(ai2)

game_ui.add_actor(life1)
game_ui.add_actor(life2)
game_ui.add_actor(life3)
game_ui.add_actor(life4)

scene.add_actor(world)
scene.add_actor(game_ui)


game = Game(scene) #, infoObject.current_w, infoObject.current_h)
game.run()
