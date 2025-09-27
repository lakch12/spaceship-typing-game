import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((50,50))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect(center=(x,y))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
