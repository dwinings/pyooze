from loader import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x = 0.0, y = 0.0, direction = "up", power =5, speed = 10):
        pygame.sprite.Sprite.__init__(self)
        self.can_move = True
        self.image = Resources.blob1tex
        self.imageList = (Resources.blob1tex,)
        if direction == "up":
            self.speed = (0, -10)
        elif direction == "left":
            self.speed = (-10, 0)
        elif direction == "right":
            self.speed = (10, 0)
        elif direction == "down":
            self.speed = (0, 10)
        self.power = power
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = direction

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
               
