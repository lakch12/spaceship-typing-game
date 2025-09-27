import pygame
from settings import *
from player import Player
from level_manager import LevelManager
from ui import draw_text, draw_input

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Typing Spaceship - Career Mode")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT-80)
level_manager = LevelManager()
current_level = level_manager.get_next_level()
typed_letters = ""
score = 0
running = True

while running:
    clock.tick(FPS)
    screen.fill(BG_COLOR)

    if not current_level.is_boss:
        current_level.spawn_enemies()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            letter = event.unicode.upper()
            typed_letters += letter
            current_level.check_letters(letter)

    player.update()
    player.draw(screen)
    current_level.update()
    current_level.draw(screen)

    draw_text(screen, f"Score: {score}", 10, 10, font)
    draw_text(screen, f"Level: {current_level.level_number}", 10, 40, font)
    draw_input(screen, typed_letters, SCREEN_WIDTH//2, SCREEN_HEIGHT-30)

    if current_level.completed():
        score += current_level.score
        current_level = level_manager.get_next_level()
        typed_letters = ""

    pygame.display.flip()

pygame.quit()
