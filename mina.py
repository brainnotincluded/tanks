from image_actor import ImageActor
import pygame


class Mina(ImageActor):
    
        def __init__(self, x, y, path = 'mina.png'):
            super().__init__(path, x, y)
            self._boom_surf = pygame.image.load('boom.png')
        def draw(self, sc):
            super().draw(sc)
            actor_collided = self.check_collision()
            if actor_collided is not None:
                print(f'BAH!!! {actor_collided}')
                from tank import Tank
                if isinstance(actor_collided, Tank):
                    print('yes')
                    if not actor_collided._life.decrease_life(20):
                        self._scene.remove_actor(actor_collided)
                        return False
                
                boom_rect = self._boom_surf.get_rect(center=(self._x, self._y))
                sc.blit(self._boom_surf, boom_rect)
                self._scene.remove_actor(self)
            return True