from loader import Resources,pygame
import random

class Tile(pygame.sprite.Sprite):
    passable = False

    #Image and rect are both required by the sprite/group subsystem
    #Images are put in a list,  and randomly picked on creation
    imageList = [Resources.defaulttex]
    image = Resources.defaulttex
    
    def __init__(self, x = 0.0, y = 0.0):
        self.pickTile()
        pygame.sprite.Sprite.__init__(self)
        self.position = (float(x), float(y))
        self.rect = self.image.get_rect(topleft=self.position)

    def __repr__(self):
        return str(self.position)
    
    def pickTile(self):
        randomPick = random.randrange(0,len(self.imageList))
        self.image = self.imageList[randomPick]

class Grass(Tile):
    passable = True
    imageList = [Resources.grass1tex,Resources.grass2tex]
    
    def __init__(self, x = 0.0, y = 0.0):
        Tile.__init__(self,x,y)
