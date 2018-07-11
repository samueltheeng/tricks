import random


class dice:
    def __init__(self, face):
        self.face = face

    def roll(self):
        return random.randint(1, self.face)
