from settings import *

text_map = [
    'WWWWWWWWWWWW',
    'WW......W..W',
    'W...WWW....W',
    'W...W......W',
    'W.......WW.W',
    'W..WW...W..W',
    'W..W..W....W',
    'WWWWWWWWWWWW'
]

world_map = {}
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        world_map[(i * TILE, j * TILE)] = char, (i, j)

print('world_map', world_map)
