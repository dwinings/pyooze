from loader import Resources,pygame
import tile

class Main:
    size = width, height = 640,480
    screen = pygame.display.set_mode(size)

    black = 0, 0, 0
    white = 255, 255, 255
    screen.fill(black)
    board = [[0 for i in range(0, 25)] for j in range(0,25)]
    background = pygame.sprite.RenderUpdates()

    def __init__(self):
        for x in range(1,(self.width / 25)):
            for y in range(1, (self.height / 25)):
                self.board[x][y] = tile.Grass(x*25.0, y*25.0)
                self.background.add(self.board[x][y])
    
    def draw(self):
        self.background.draw(self.screen)
        pygame.display.flip()

    def update(self):
        try:
            self.draw()
        except TypeError:
            print "wtf"
            #secret


def main():
    thegame = Main()
    while 1:
        thegame.update()

    youlost(thegame)

def youlost(a):
    print "Hahaha"

if __name__ == "__main__":
    main()
