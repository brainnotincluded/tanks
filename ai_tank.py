import copy

from pygame.surface import Surface

from tank import Tank


class AITank(Tank):

    def __init__(self, path, x, y, joy, life):
        super().__init__(path, x, y, {}, joy, life)
        self._map = AITank.read_map('ai.txt')
        self._size = (len(self._map), len(self._map[0]))

    def draw(self, sc: Surface):
        self._think()
        super().draw(sc)
        return True

    def _think(self):
        karta, i, j = self._make_wave(target=(1, 1))
        self._backtrack(karta, i, j)
        pass

    def _make_wave(self, target):
        karta = copy.deepcopy(self._map)
        i = self._y//50
        j = self._x//50
        karta[i][j] = 0
        t_i, t_j = target
        front = [(i, j)]
        while True:
            front2 = []
            for i_, j_ in front:
                if i_ == t_i and j_ == t_j:
                    return karta, i, j
                for n_i, n_j in self.near(i_,  j_):
                    if karta[n_i][n_j] == '.':
                        karta[n_i][n_j] = karta[i_][j_] + 1
                        front2.append((n_i, n_j))
            front = front2
    def handle_joykeys(self):
        pass
    def _backtrack(self, karta, i, j):
        return []

    def near(self, i, j):
        h, w = self._size
        l = [(i, j-1), (i, j+1), (i - 1, j), (i + 1, j)]
        return [(i_, j_) for i_, j_ in l if h > i_ >= 0 and w > j_ >= 0 and self._map[i_][j_] == '.']

    def handle_keys(self, keys):
        pass

    @staticmethod
    def read_map(path):
        with open(path, "r") as f:
            txt = f.read()
        karta = []
        for i, line in enumerate(txt.split()):
            karta += [[]]
            for j, c in enumerate(line):
                karta[i] += [c]
        return karta




if __name__ == '__main__':
    karta = AITank.read_map('map_z.txt')
    karta = copy.deepcopy(karta)