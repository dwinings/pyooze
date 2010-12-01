from loader import *

class Player(pygame.sprite.Sprite):
    imageList = (Resources.playerUPtex, Resources.playerDOWNtex ,Resources.playerRIGHTtex,Resources.playerLEFTtex )
    def __init__(self, x=0.0, y = 0.0):
        pygame.sprite.Sprite.__init__(self)
        self.image = Resources.playerUPtex
        self.inertia = [0.0, 0.0]
        self.max_inertia = (10.0, 10.0)
        self.speed = (0.3)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.goocount = 20
    
    def update_inertia(self):
        self.move()
        if self.inertia[0] < 0:
            self.inertia[0] += 0.1
        elif self.inertia[0] > 0:
            self.inertia[0] -= 0.1
            
        if self.inertia[1] < 0:
            self.inertia[1] += 0.1
        if self.inertia[1] > 0:
            self.inertia[1] -= 0.1
            
        if abs(self.inertia[0]) <= 0.1:
            self.inertia[0] = 0.0
        if abs(self.inertia[1]) <= 0.1:
            self.inertia[1] = 0.0
            
                
        
    def add_inertia(self, x=0.0, y=0.0):
        self.inertia[0] += x
        self.inertia[1] += y

    def move(self):
        if self.can_move():
            self.rect.x += self.inertia[0]
            self.rect.y += self.inertia[1]
        else:
            self.inertia = [0,0]

    def can_move(self):
        if 1==1:#placeholder
            return True 
        else:
            return False

    def rotate(self, direction):
        if direction == "up":
            self.image = self.imageList[0]
        elif direction == "down":
            self.image = self.imageList[1]
        elif direction == "left":
            self.image = self.imageList[2]
        else:
            self.image = self.imageList[3]
        

    
        
