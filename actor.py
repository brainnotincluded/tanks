from pygame.surface import Surface
from typing import List
from pygame import Rect

class Actor:
    
    def set_game(self, game):
        pass
    
    def draw(self, sc: Surface) -> bool:
        raise NotImplementedError
    
    def handle_keys(self, keys):
        pass
    
    def handle_joystick(self, jevent):
        pass
    
    def get_rect(self) -> Rect:
        return None