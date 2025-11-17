import random
from sty import fg

def color(word:str):

    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    result = fg(red, green, blue)
    print(f'{result}{word}{fg.rs}')

color("Hello")