import random

names = ["Mickey", "Donald", "Minnie", "Pluto"]

while len(names) > 0:
    name = random.choice(names)
    print(name)
    names.remove(name)
