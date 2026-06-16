import pygame

class Enemy:
    def __init__(self, x, y, player):
        self.stats = {
            "max_hp": 100,
            "hp": 100,
            "speed": 200,
            "damage": 10
        }

    def update(self, dt):
        pass

    def draw(self, screen, camera):
        pass