from loader import *
import random

class Tile(pygame.sprite.Sprite):
    """This is a class terrain types will inherit from. It's not meant to be used"""    
    passable = False

    #Image and rect are both required by the sprite/group subsystem
    #Images are put in a list,  and randomly picked on creation
    imageList = (Resources.defaulttex,)
    image = Resources.defaulttex
    
    
    def __init__(self, x = 0.0, y = 0.0):
        self.pickTile()
        pygame.sprite.Sprite.__init__(self)
        self.position = (float(x), float(y))
        self.rect = self.image.get_rect(topleft=self.position)

    def __repr__(self):
        return str(self.position)
    
    def pickTile(self):
        self.image = random.choice(self.imageList)

class Grass(Tile):
    passable = True
    imageList = (Resources.grass1tex, Resources.grass2tex)
    
    def __init__(self, x = 0.0, y = 0.0):
        Tile.__init__(self,x,y)

class Rock(Tile):
    passable = False
    imageList = (Resources.rock1tex, Resources.rock2tex)
    
    def __init__(self, x=0.0, y=0.0):
        Tile.__init__(self,x,y)
