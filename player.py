from loader import *
class Player(pygame.sprite.Sprite):
    def __init__(self, x=0.0, y = 0.0):
        pygame.sprite.Sprite.__init__(self)
        self.position = [x, y]
        self.image = Resources.playertex
        self.rect = self.image.get_rect(topleft=self.position)
        self.goocount = 20
        

    def Move( x=0.0, y=0.0 ):
        self.position[0] += x
        self.position[1] += y

    
        
