from loader import Resources,pygame
import random

class Tile(pygame.sprite.Sprite):
    passable = False

    #Image and rect are both required by the sprite/group subsystem
    image = Resources.defaulttex
    
    def __init__(self, x = 0.0, y = 0.0):
        pygame.sprite.Sprite.__init__(self)
        self.position = (float(x), float(y))
        self.rect = self.image.get_rect(topleft=self.position)

    def __repr__(self):
        return str(self.position)

class Grass(Tile):
    passable = True
    image = Resources.grass2tex
    choice = 0
    def __init__(self, x = 0.0, y = 0.0):
        Grass.pickTile(self)
        Tile.__init__(self,x,y)

    def pickTile(self):
        choice = random.randrange(0,2)
        if choice == 0:
            self.image = Resources.grass1tex
        else:
            self.image = Resources.grass2tex

