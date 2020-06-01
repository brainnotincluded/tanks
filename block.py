from image_actor import ImageActor


class Block(ImageActor):
    
    def __init__(self, x, y, path = 'C:\\Users\\vorob\\Pictures\\Saved Pictures\\block.png'):
        super().__init__(path, x, y)