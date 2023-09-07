# pseudo random numbers

import random

x = random.randint(1, 6)
print(x)

y = random.random()  # random floats
print(y)

my_list = ["rock", "paper", "scissor"]
z = random.choice(my_list)
print(z)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "j", "q", "k", "a"]
random.shuffle(cards)

print(cards)
