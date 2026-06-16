import pygame

class Player:
    def __init__(self, x, y):
        self.stats = {
            "max_hp": 100,
            "hp": 100,
            "walk": 200,
            "run": 400,
            "damage": 100
        }

    def handle_input(self, dt):
        pass

    def update(self, dt):
        pass

    def draw(self, screen, camera):
        pass