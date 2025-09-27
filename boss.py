import pygame

class Boss:
    def __init__(self, x, y, word):
        self.image = pygame.Surface((120,80))
        self.image.fill((255,100,0))
        self.rect = self.image.get_rect(center=(x,y))
        self.word = word
        self.destroyed = False
        self.speed = 0.5

    def update(self):
        self.rect.x += self.speed
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.speed *= -1

    def hit(self, letter):
        self.word = self.word.replace(letter,"")
        if len(self.word)==0:
            self.destroyed = True

    def draw(self, screen):
        screen.blit(self.image,self.rect)
        font = pygame.font.SysFont("Arial",24)
        text = font.render(self.word,True,(255,255,0))
        screen.blit(text,(self.rect.x+10,self.rect.y+20))
