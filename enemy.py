import pygame

class Enemy:
    def __init__(self, x, y, word):
        self.image = pygame.Surface((60,40))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center=(x,y))
        self.word = word
        self.destroyed = False
        self.speed = 1

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 600:
            self.destroyed = True

    def hit(self, letter):
        self.word = self.word.replace(letter,"")
        if len(self.word) == 0:
            self.destroyed = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        font = pygame.font.SysFont("Arial",20)
        text = font.render(self.word,True,(255,255,255))
        screen.blit(text,(self.rect.x+5,self.rect.y+5))
