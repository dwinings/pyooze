from loader import *

class Projectile(pygame.sprite.Sprite):
    can_move = True
    image = Resources.defaulttex
    imageList = (Resources.defaulttex,)
    friendly = True #distingueshes player projectiles form enemy ones
    damage = 0 
    base_speed = 0
    
    def __init__(self, x = 0.0, y = 0.0, direction = "up"):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = direction
        if direction == "up":
            self.speed = (0, -1 *self.base_speed)
        elif direction == "left":
            self.speed = (-1 * self.base_speed, 0)
        elif direction == "right":
            self.speed = (self.base_speed, 0)
        elif direction == "down":
            self.speed = (0, self.base_speed)
       
    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
               
class SmallBlob(Projectile):
    image = Resources.blob1tex
    imageList = (Resources.blob1tex,)
    friendly = True
    base_speed = 10
    damage = 10
    def __init__(self,  x = 0.0, y = 0.0, direction = "up"):
        Projectile.__init__(self, x, y, direction)
