from loader import *
import player
import tile


class Main:
    size = width, height = 640,480
    fps = 60
    pygame.display.set_icon(Resources.playerUPtex)
    screen = pygame.display.set_mode(size, HWSURFACE)
    
    keys = {'up': False, 'down': False, 'left': False, 'right': False}
    black = 0, 0, 0
    white = 255, 255, 255
    red = 255,0,0
    yellow = 0,0,255
    screen.fill(black)
    mapfile = 'Maps/default.map'
    player = player.Player(30.0, 30.0)
    board = []
    background = pygame.sprite.RenderUpdates()
    obstacles = pygame.sprite.RenderUpdates()
    sprites = pygame.sprite.RenderUpdates()
    mapfileparser = {
                    '0': tile.Grass,
                    '1': tile.Rock
                    }

    def __init__(self):
        mapfile = open(self.mapfile, 'r') # Add Exception Handler later.
        self.convert_textures() 
        self.sprites.add(self.player)
        x= 0
        y = 0
        temp = []
        for line in mapfile:
            line = line.rstrip('\n')
            for char in line:
                tile = self.mapfileparser[char](x*25.0, y*25.0)
                temp.append(tile)
                self.background.add(tile)
                if tile.passable == False:
                    self.obstacles.add(tile)
                x += 1
                
            self.board.append(temp)
            temp = []                
            y += 1
            x = 0
    
    def convert_textures(self):
        Resources.grass2tex = Resources.grass2tex.convert()
        Resources.rock1tex = Resources.rock1tex.convert()
        Resources.rock2tex = Resources.rock1tex.convert()
        Resources.defaulttex = Resources.defaulttex.convert()
        Resources.dirt1tex = Resources.dirt1tex.convert()
        Resources.playerUPtex = Resources.playerUPtex.convert()
        Resources.playerDOWNtex = Resources.playerDOWNtex.convert()
        Resources.playerRIGHTtex = Resources.playerRIGHTtex.convert()
        Resources.playerLEFTtex = Resources.playerLEFTtex.convert()
        Resources.gootex = Resources.gootex.convert()
    
    def draw(self):
        rect_list = self.background.draw(self.screen)
        self.sprites.draw(self.screen)
        pygame.display.update(rect_list)
        
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
            self.player.rotate("up")
        if self.keys['down']:
            self.player.add_inertia(y=self.player.speed)
            self.player.rotate("down")
        if self.keys['right']:
            self.player.add_inertia(x=self.player.speed)
            self.player.rotate("right")
        if self.keys['left']:
            self.player.add_inertia(x=-self.player.speed)
            self.player.rotate("left")
            
    def handle_collisions(self):
        if pygame.sprite.spritecollideany(
                player.RectHolder(self.player.rect.x + self.player.inertia[0], 
                                  self.player.rect.y + self.player.inertia[1], 
                                  25, 
                                  25), self.obstacles):

            self.player.can_move = False
        else: self.player.can_move = True

    def update(self):
        self.handle_events()
        self.handle_movement()
        self.handle_collisions()
        self.player.update()
        self.draw()
            


def main():
    thegame = Main()
    main_clock = pygame.time.Clock()
    while 1:
        main_clock.tick(thegame.fps)
        thegame.update()

if __name__ == "__main__":
    main()
