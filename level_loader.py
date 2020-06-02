from block import Block
from mina import Mina


class LevelLoader:
    
    def __init__(self, path, scene):
        with open(path, "r") as f:
            txt = f.read()
        
        
        for i, line in enumerate(txt.split()):
            for j, c in enumerate(line):
                if c == 'o':
                    scene.add_actor(Block(j*50+25, i*50+25))
                if c == 'x':
                    scene.add_actor(Mina(j*50+25, i*50+25))

if __name__ == '__main__':
    LevelLoader('map_z.txt')