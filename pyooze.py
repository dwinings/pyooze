from loader import *
import player
import tile

class Main:
    size = width, height = 640,480
    screen = pygame.display.set_mode(size)
    keys = {'up': False, 'down': False, 'left': False, 'right': False}
    black = 0, 0, 0
    white = 255, 255, 255
    red = 255,0,0
    yellow = 0,0,255
    screen.fill(black)
    mapfile = 'Maps/default.map'
    player = player.Player(30.0, 30.0)
    board = [[0 for i in range(0, 25)] for j in range(0,25)]
    background = pygame.sprite.RenderUpdates()
    sprites = pygame.sprite.RenderUpdates()
    mapfileparser = {
                    '0': tile.Grass,
                    '1': tile.Rock
                    }

    def __init__(self):
        mapfile = open(self.mapfile, 'r') # Add Exception Handler later.
        self.sprites.add(self.player)
        x = 0
        y = 0
        for line in mapfile:
            line = line.rstrip('\n')
            for char in line:
                self.board[x][y] = self.mapfileparser[char](x*25.0, y*25.0)
                self.background.add(self.board[x][y])
                x += 1
            y += 1
            x = 0
    
    def draw(self):
        self.background.draw(self.screen)
        self.sprites.draw(self.screen)
        pygame.display.flip()
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_UP:
                    self.keys['up'] = True
                if event.key == K_DOWN:
                    self.keys['down'] = True
                if event.key == K_LEFT:
                    self.keys['left'] = True
                if event.key == K_RIGHT:
                    self.keys['right'] = True
                    
            if event.type == KEYUP:
                if event.key == K_UP:
                    self.keys['up'] = False
                if event.key == K_DOWN:
                    self.keys['down'] = False
                if event.key == K_LEFT:
                    self.keys['left'] = False
                if event.key == K_RIGHT:
                    self.keys['right'] = False
                    
    def handle_movement(self):
        if self.keys['up']:
            self.player.add_inertia(y=-self.player.speed)
        if self.keys['down']:
            self.player.add_inertia(y=self.player.speed)
        if self.keys['right']:
            self.player.add_inertia(x=self.player.speed)
        if self.keys['left']:
            self.player.add_inertia(x=-self.player.speed)
        

    def update(self):
        self.handle_events()
        self.handle_movement()
        self.player.update_inertia()
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

if __name__ == "__main__":
    main()
