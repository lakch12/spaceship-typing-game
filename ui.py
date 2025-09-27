import pygame

def draw_text(screen,text,x,y,font,color=(255,255,255)):
    surface = font.render(text,True,color)
    screen.blit(surface,(x,y))

def draw_input(screen,text,x,y):
    font = pygame.font.SysFont("Arial",24)
    surface = font.render(text,True,(0,255,255))
    rect = surface.get_rect(center=(x,y))
    screen.blit(surface,rect)
