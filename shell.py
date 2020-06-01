from image_actor import ImageActor
import pygame



class Shell(ImageActor):
    
    def __init__(self, x, y, vx, vy, tank):
        super().__init__('C:\\Users\\vorob\\Pictures\\Saved Pictures\\shell.png', x, y)
        self._tank = tank
        self._vx = vx
        self._vy = vy
        self._n = 0
        
    def draw(self, sc):
        self._n += 1
        
        super().draw(sc)
        self._update_xy()
        
        if self._n > 50:
            return False
        
        actor_collided = self.check_collision()
        
        if actor_collided is not None and actor_collided != self._tank:
            print(f'BAH!!! {actor_collided}')
            from tank import Tank
            if isinstance(actor_collided, Tank):
                print('yes')
                if not actor_collided._life.decrease_life():
                    self._scene.remove_actor(actor_collided)
            boom_surf = pygame.image.load('C:\\Users\\vorob\\Pictures\\Saved Pictures\\boom.png')
            boom_rect = boom_surf.get_rect(center=(self._x, self._y))
            sc.blit(boom_surf, boom_rect)
            self._scene.remove_actor(self)
        
        return True
        
    def _update_xy(self):
        self._x += self._vx
        self._y -= self._vy
        