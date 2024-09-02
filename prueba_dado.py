import random

def dice():
    dado = []
    for i in range(100):
        dado.append(random.choice(range(1,7)))
        return dado

dice()