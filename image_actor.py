from pygame.surface import Surface
from actor import Actor 
import pygame
import math


class ImageActor(Actor):
    
    def __init__(self, path, x, y):
        self._surf = pygame.image.load(path)
        self._x = x
        self._y = y
        self._a = 0
        self._surf2 = pygame.transform.rotate(self._surf, -self._a)
        self._rect = self._surf2.get_rect(center=(self._x, self._y))
        self._game = None
        self._scene = None

    def set_game(self, game):
        self._game = game
        
    def set_center(self, x, y):
        self._x = x
        self._y = y
        
    def draw(self, sc: Surface):
        self._surf2 = pygame.transform.rotate(self._surf, self._a)
        self._rect = self._surf2.get_rect(center=(self._x, self._y))
        sc.blit(self._surf2, self._rect)
        
        return True
    
    def set_scene(self, scene):
        self._scene = scene
        
    def handle_keys(self, keys):
        pass
    
    def get_rect(self):
        return self._rect
    
    def check_collision(self):
        actors, rects = self._scene.get_actors_rects(self)
        #print(f'ACTORS: {actors}')
        #print(f'RECTS: {rects}')
        i = self._rect.collidelist(rects)
        if i == -1:
            return None
        else:
            return actors[i]
        
        