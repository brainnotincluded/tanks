from pygame.surface import Surface
from game import Game
import pygame
from image_actor import ImageActor
import math
from scene import Scene
from shell import Shell
from block import Block
from level_loader import LevelLoader
from life_bar import LifeBar


class Tank(ImageActor):
    def __init__(self, path, x, y, key_map, joy, life):
        super().__init__(path, x, y)
        self._old_x = self._x
        self._old_y = self._y
        self._v = -5
        self._va = 3
        self._key_map = key_map
        self._joy = joy
        self.vx_vy_update()
        self._life = life
    def draw(self, sc: Surface):
        self._surf2 = pygame.transform.rotate(self._surf, self._a)
        self._rect = self._surf2.get_rect(center=(self._x, self._y))
    
        #
        actor_collided = self.check_collision()
        if actor_collided is not None and not isinstance(actor_collided, Shell):
            self._x = self._old_x
            self._y = self._old_y
            self._rect = self._surf2.get_rect(center=(self._x, self._y))
    
        #
        sc.blit(self._surf2, self._rect)

        self.handle_joykeys()
        return True
         
    def handle_joykeys(self):
        #print(f'{self._game._joysticks}')
        #print(f'{self._joy}')
        j = self._game._joysticks[self._joy]
        if j.get_axis(0) > 0.5:
            self._a -= self._va
            self.vx_vy_update()
        elif j.get_axis(0) < -0.5:
            self._a += self._va
            self.vx_vy_update()
            
        self._old_x = self._x
        self._old_y = self._y
        if j.get_axis(1) > 0.5:
            self._x -= self._vx
            self._y += self._vy
        elif j.get_axis(1) < -0.5:
            self._x += self._vx
            self._y -= self._vy
        
        
        #if j.get_button(5):
        #    print('yes')
            
            
            
    def vx_vy_update(self):
        
        self._vx = -self._v * math.cos(math.pi/180 * self._a)
        self._vy = -self._v * math.sin(math.pi/180 * self._a)
        
    def handle_joystick(self, j):
        if j.joy != self._joy:
            return
        
        print(f'J-EVENT: {j}')
        
        if hasattr(j, 'button') and j.button == 5:
            shell = Shell(self._x, self._y, self._vx * 3, self._vy * 3, self)
            self._scene.add_actor(shell)
        pass
    
    def handle_keys(self, keys):
        if keys [self._key_map['l']]:
                self._a -= self._va
                self.vx_vy_update()
        elif keys [self._key_map['r']]:
                self._a += self._va
                self.vx_vy_update() 

        if keys [self._key_map['u']]:
                self._x += self._vx
                self._y += self._vy
        elif keys [self._key_map['d']]:
                self._x -= self._vx
                self._y -= self._vy
        rect = self._surf2.get_rect()
        w = rect.width / 2
        h = rect.height / 2
        self._x = min(self._x,self._game.width-w-2)
        self._x = max(self._x,0+w+2)
        self._y = min(self._y,self._game.height-h-2)
        self._y = max(self._y,0+h+2)
    

if __name__ == '__main__':
    life1 = LifeBar(5, 2, (0,150,0))
    life2 = LifeBar(1095, 2, (255,0,0))
    tank1 = Tank(
        'C:\\Users\\vorob\\Pictures\\Saved Pictures\\kub3.png',
        0, 800,
        {'u': pygame.K_w,
         'd': pygame.K_s,
         'l': pygame.K_a,
         'r': pygame.K_d
         }, 0, life1)
    tank2 = Tank(
        'C:\\Users\\vorob\\Pictures\\Saved Pictures\\kub4.png',
        1200, 800,
        {'u': pygame.K_UP,
         'd': pygame.K_DOWN,
         'l': pygame.K_LEFT,
         'r': pygame.K_RIGHT}, 1, life2)
    scene = Scene()
    game_ui = Scene()
    
    world = Scene()
    world.add_actor(tank1)
    world.add_actor(tank2)
    
    game_ui.add_actor(life1)
    game_ui.add_actor(life2)
    
    scene.add_actor(world)
    scene.add_actor(game_ui)
    
    LevelLoader('C:\\Users\\vorob\\Documents\\python_files\\map_daniil.txt', world)
    game = Game(scene, 1200, 800)
    game.run()