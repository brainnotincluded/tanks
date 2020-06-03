import pygame


class Game:
    def __init__(self, actor, w, h):
        self._actor = actor
        self._actor.set_game(self)
        pygame.init()
        pygame.joystick.init()
        self._joysticks = []
        for x in range(pygame.joystick.get_count()):
            j = pygame.joystick.Joystick(x)
            j.init()
            self._joysticks.append(j)
        print(self._joysticks)
        self._sc = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
        self.width = w
        self.height = h
        
    def run(self):
        while True:
            for i in pygame.event.get():
                if hasattr(i, 'joy'):
                    print(i.joy)
                    self._actor.handle_joystick(i)        
                if i.type == pygame.QUIT:
                    exit()
            # очищаем экран
            self._sc.fill((0, 0, 0))
            # реакция на клавиши
            keys = pygame.key.get_pressed()
            self._actor.handle_keys(keys)
            # рисуем актёра
            self._actor.draw(self._sc)
            # обновляем экран
            pygame.display.update()
            # задержка
            pygame.time.delay(30)







