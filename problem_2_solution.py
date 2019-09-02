# Stefan Manuel Anderson - stefananderson06@gmail.com

location = {'x' : 0, 'y' : 0}

while True:
    movement = input().lower()
    if movement == '':
        break
    elif movement == 'up':
        location['x'] += 1
    elif movement == 'down':
        location['x'] -= 1
    elif movement == 'left':
        location['y'] -= 1
    elif movement == 'right':
        location['y'] += 1

print('Coordinate :', location)
x = location['x']
y = location['y']

location_now = (x ** 2 + y ** 2) ** 0.5

location_now = round(location_now)

print('Distance :', location_now)
