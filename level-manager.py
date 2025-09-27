from enemy import Enemy
from boss import Boss
import random

class Level:
    def __init__(self, level_number, chapter, words, is_boss=False):
        self.level_number = level_number
        self.chapter = chapter
        self.words = words
        self.enemies = []
        self.is_boss = is_boss
        self.completed_flag = False
        self.score = 0

    def spawn_enemies(self):
        if len(self.enemies) < 5 and not self.is_boss:
            word = random.choice(self.words)
            x = random.randint(50,750)
            self.enemies.append(Enemy(x,50,word))
        if self.is_boss and not self.enemies:
            self.enemies.append(Boss(400,100,random.choice(self.words)))

    def check_letters(self, letter):
        for enemy in self.enemies:
            if letter in enemy.word:
                enemy.hit(letter)

    def update(self):
        for enemy in self.enemies[:]:
            enemy.update()
            if enemy.destroyed:
                self.enemies.remove(enemy)
                self.score += 10
        if not self.enemies:
            self.completed_flag = True

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def completed(self):
        return self.completed_flag

class LevelManager:
    def __init__(self):
        self.chapters = 12
        self.levels_per_chapter = 50
        self.current_chapter = 1
        self.current_level_num = 1
        self.words = ["STAR","MOON","PLANET","ASTEROID","COMET","ROCKET"]

    def get_next_level(self):
        is_boss = self.current_level_num % 10 == 0
        level = Level(self.current_level_num,self.current_chapter,self.words,is_boss)
        self.current_level_num += 1
        if self.current_level_num > self.levels_per_chapter:
            self.current_level_num = 1
            self.current_chapter += 1
        return level
