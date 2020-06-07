import math

from ai_tank import AITank
from shell import Shell
from tank import Tank


class Turele(AITank):
    def __init__(self, path, x, y, joy, life):
        super().__init__(path, x, y, joy, life)
        self._n = 1

    def _norm_degrees(self):
        self._a %= 360
        if self._a > 180:
            self._a -= 360

    def _think(self):
        self._n += 1
        self._norm_degrees()
        target, a = self._seek_target()
        if self._n % 4 == 0:
            self._shoot()
        if target is not None:
            sign = 1
            if abs(a - self._a) > 180:
                sign = -1
            if a > self._a:
                self._a += 3 * sign
            else:
                self._a -= 3 * sign
            self.vx_vy_update()

    def _shoot(self):
        shell = Shell(self._x, self._y, self._vx * 3, self._vy * 3, self)
        self._scene.add_actor(shell)

    def _seek_target(self):
        min_dist = 9999999999
        target = None
        a = 0
        for actor in self._scene.get_actors():
            if isinstance(actor, Tank) and actor != self:
                kx = actor._x - self._x
                ky = actor._y - self._y
                dist = math.hypot(kx, ky)
                if dist < min_dist:
                    rad = math.atan2(-ky, kx)
                    a = math.degrees(rad)
                    min_dist = dist
                    target = actor
        return target, a

