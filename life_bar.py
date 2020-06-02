from actor import Actor
import pygame

class LifeBar(Actor):
    def __init__(self, x, y, color):
        self._color = color
        self._x = x
        self._y = y
        self._value = 100
    
    def draw(self, sc):
        pygame.draw.rect(sc, (0, 255, 0), (self._x, self._y, self._value, 30))
        pygame.draw.rect(sc, self._color, (self._x, self._y, 100, 30), 3)
        return True
        
    def set_scene(self, scene):
        pass
    
    def decrease_life(self, uron) -> bool:
        self._value -= uron
        if self._value <= 0:
            return False
        return True
            
        