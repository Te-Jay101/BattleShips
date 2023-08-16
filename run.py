import random


class Board:
    def __init__(self, size, owner):
        self.size = size
        self.grid = [['O' for _ in range(size)] for _ in range(size)]
        self.owner = owner