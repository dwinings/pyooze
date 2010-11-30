from loader import *
import tile
from player import *

class Main:
    size = width, height = 640,480
    screen = pygame.display.set_mode(size)

    black = 0, 0, 0
    white = 255, 255, 255
    red = 255,0,0
    yellow = 0,0,255
    screen.fill(black)
    player = Player(30.0, 30.0)
    board = [[0 for i in range(0, 25)] for j in range(0,25)]
    background = pygame.sprite.RenderUpdates()
    sprites = pygame.sprite.RenderUpdates()

    def __init__(self):
        self.sprites.add(self.player)
        for x in range(1,(self.width / 25)):
            for y in range(1, (self.height / 25)):
                self.board[x][y] = tile.Grass(x*25.0, y*25.0)
                self.background.add(self.board[x][y])
    
    def draw(self):
        self.background.draw(self.screen)
        self.sprites.draw(self.screen)
        pygame.display.flip()

    def update(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_UP:
                    pass
                if event.key == K_DOWN:
                    pass
                if event.key == K_LEFT:
                    self.player.Move(x=-1.0)
                if event.key == K_RIGHT:
                    pass
        try:
            self.draw()
        except TypeError:
            print "wtf"


def main():
    thegame = Main()
    main_clock = pygame.time.Clock()
    while 1:
        main_clock.tick(30)
        thegame.update()

    youlost(thegame)

def youlost(a):
    print "Hahaha"

if __name__ == "__main__":
    main()
