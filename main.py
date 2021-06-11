import pygame

pygame.init()

clock = pygame.time.Clock()

width, height = 1024, 480
window = pygame.display.set_mode((width, height), pygame.RESIZABLE)

class Events:

    def __init__(self):
        self.stopStatus = False
        self.events = []

        #deltaTime
        self.lastFrame = pygame.time.get_ticks() / 1000.0
        self.currentFrame = ""

    
    def update(self):
        self.events = pygame.event.get()

        for e in self.events:
            if e.type == pygame.VIDEORESIZE:
                window = pygame.display.set_mode((e.w, e.h), pygame.RESIZABLE)
                width, height = e.w, e.h
            if e.type == pygame.QUIT:
                self.stopStatus = True

        #Deltatime calculations
        self.currentFrame = pygame.time.get_ticks() - self.lastFrame
        self.lastFrame = pygame.time.get_ticks()
    
    def flushEvents(self):
        self.events = []

class Player:

    def __init__(self, defaultKey=False):
        self.pos = [width//2,height//2]
        self.key = defaultKey
        self.speed = 0.02
        self.compass = 0

        self.sprite = pygame.image.load("Player.png")

    def update(self, eventObject):
        key = pygame.key.get_pressed()
        
        if self.key == True:
            if key[pygame.K_w]:
                self.compass = 0
                self.pos[1] -= 16 * eventObject.currentFrame
            elif key[pygame.K_s]:
                self.compass = 180
                self.pos[1] += 16 * eventObject.currentFrame
            elif key[pygame.K_a]:
                self.compass = 270
                self.pos[0] -= 16 * eventObject.currentFrame
            elif key[pygame.K_d]:
                self.compass = 90
                self.pos[0] += 16 * eventObject.currentFrame
        else:
            if key[pygame.K_UP]:
                self.compass = 0
                self.pos[1] -= 1 * eventObject.currentFrame
            elif key[pygame.K_DOWN]:
                self.compass = 180
                self.pos[1] += 1 * eventObject.currentFrame
            elif key[pygame.K_LEFT]:
                self.compass = 270
                self.pos[0] -= 1 * eventObject.currentFrame
            elif key[pygame.K_RIGHT]:
                self.compass = 90
                self.pos[0] += 1 * eventObject.currentFrame

        #Draw Sprite
        if self.compass == 0:
            window.blit(self.sprite, self.pos, (0, 32, 16, 16))
        if self.compass == 90:
            window.blit(self.sprite, self.pos, (0, 48, 16, 16))
        if self.compass == 180:
            window.blit(self.sprite, self.pos, (0, 0, 16, 16))
        if self.compass == 270:
            window.blit(self.sprite, self.pos, (0, 16, 16, 16))



class Game:

    def __init__(self):
        self.eventObject = Events()
        self.playerObject = Player()

    def draw(self):
        while self.eventObject.stopStatus == False:
            window.fill((0,0,240))
            self.eventObject.update()
            self.playerObject.update(self.eventObject)

            pygame.display.flip()
            self.eventObject.flushEvents()



if __name__ == "__main__":
    game = Game()
    game.draw()