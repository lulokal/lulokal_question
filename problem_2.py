"""
    Ginus Pandhu Setyawna
    ginus_pandhu@hotmail.com / 082282227625
"""

import math

zero_position = {'x': 0, 'y': 0}
coordinat = {'x': 0, 'y': 0}
print('UP: ')
up_move = int(input())
print('DOWN: ')
down_move = int(input())
print('LEFT: ')
left_move = int(input())
print('RIGHT: ')
right_move = int(input())

if up_move:
    coordinat['y'] += up_move
if down_move:
    coordinat['y'] -= down_move
if left_move:
    coordinat['x'] -= left_move
if right_move:
    coordinat['x'] += right_move

x_handle = (coordinat['x'] ** 2) - (zero_position['x'] ** 2)
y_handle = (coordinat['y'] ** 2) - (zero_position['y'] ** 2)
find_distance = math.sqrt(x_handle + y_handle)

print(round(find_distance))
