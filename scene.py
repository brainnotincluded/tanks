from pygame.surface import Surface

from actor import Actor


class Scene(Actor):

    def __init__(self):
        self._actors = []
        self._game = None
        self._scene = None

    def draw(self, sc: Surface):
        to_remove = []

        for actor in self._actors.copy():
            if not actor.draw(sc):
                to_remove.append(actor)
                
        for actor in to_remove:
            self._actors.remove(actor)
            
        return True

    def handle_keys(self, keys):
        for actor in self._actors.copy():
            actor.handle_keys(keys)

    def set_game(self, game):
        self._game = game
        for actor in self._actors.copy():
            actor.set_game(game)
        
    def add_actor(self, actor):
        self._actors.append(actor)
        if self._game is not None:
            actor.set_game(self._game)
        
        actor.set_scene(self)

    def remove_actor(self, actor):
        self._actors.remove(actor)
        
    def handle_joystick(self, j):
        for actor in self._actors.copy():
            actor.handle_joystick(j)
    
    def get_actors(self):
        return self.actors
    
    def get_actors_rects(self, exclude_actor):
        actors = [actor for actor in self._actors if actor != exclude_actor]
        rects = [actor.get_rect() for actor in actors]
        return actors, rects

    def set_scene(self, scene):
        self._scene = scene