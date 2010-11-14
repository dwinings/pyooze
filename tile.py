from loader import Resources,pygame

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
    def __init__(self, x = 0.0, y = 0.0):
        Tile.__init__(self,x,y)

