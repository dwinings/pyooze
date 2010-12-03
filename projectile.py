from loader import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x = 0.0, y = 0.0,direction = "up" ,speed_x_boost = 0, speed_y_boost = 0):
        pygame.sprite.Sprite.__init__(self)
        self.can_move = True
        self.image = Resources.blob1tex
        self.imageList = (Resources.blob1tex,)
        self.speed = 10
        self.rect = self.image.get_rect(topleft=(x, y))
        self.tile = (0,0)
        self.direction = direction
        self.speed_y_boost = speed_y_boost
        self.speed_x_boost = speed_x_boost

    def update(self):
        if self.can_move:
              self.move()
        else: print "nyi"
                
    def move(self):
        if self.direction == "up":
            self.rect.y -= self.speed + abs(self.speed_y_boost)
        elif self.direction == "down":
            self.rect.y += self.speed  + abs(self.speed_y_boost)
        elif self.direction == "left":
            self.rect.x -= self.speed + abs(self.speed_x_boost)
        else:
            self.rect.x += self.speed + abs(self.speed_x_boost)
               
class RectHolder():
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
    
