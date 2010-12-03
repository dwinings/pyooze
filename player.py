from loader import *

class Player(pygame.sprite.Sprite):

    def __init__(self, x=0.0, y = 0.0):
        pygame.sprite.Sprite.__init__(self)
        self.can_move = True
        self.image = Resources.playerUPtex
        self.imageList = (Resources.playerUPtex, Resources.playerDOWNtex ,Resources.playerRIGHTtex,Resources.playerLEFTtex )
        self.inertia = [0.0, 0.0]
        self.max_inertia = (10.0, 10.0)
        self.speed = (0.3)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.goocount = 6
        self.tile = (0,0)
        self.direction = "up"
    
    def update(self):
        if self.can_move:
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
        else: self.inertia = [0.0, 0.0]
                
        
    def add_inertia(self, x=0.0, y=0.0):
        self.inertia[0] += x
        self.inertia[1] += y

    def move(self):
        self.rect.x += self.inertia[0]
        self.rect.y += self.inertia[1]
        
    def update_tile(self):
        tile= (int((self.rect.x + 12.5) / 25), int((self.rect.y + 12.5) /25))
        if tile != self.tile:
            self.tile = tile
            return tile
        else: return False

    def rotate(self, direction):
        if direction == "up":
            self.image = self.imageList[0]
            self.direction = "up"
        elif direction == "down":
            self.image = self.imageList[1]
            self.direction = "down"
        elif direction == "left":
            self.image = self.imageList[2]
            self.direction = "left"
        else:
            self.image = self.imageList[3]
            self.direction = "right"
        
class RectHolder():
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
    
        
