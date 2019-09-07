'''
run = python solving2.py
and you can input with command = UP (value), DOWN (value), RIGHT (value), LEFT (value)
example = UP 5
*Note = just separate use space
and enter will close or end input
                                    '''
START_POINTS = (0,0) #x,y
end_points = [0,0]
def get_distance(start,end):
    dist = ((end[0] - start[0]) + (end[1] - start[1])) ** 0.5
    return dist
while True:
    move_point = raw_input().upper()
    move = move_point.split(' ')
    if move[0] == 'UP':
        end_points[1] += int(move[1])
    elif move[0] == "DOWN":
        end_points[1] -= int(move[1])
    elif move[0] == "RIGHT":
        end_points[0] += int(move[1])
    elif move[0] == "LEFT":
        end_points[0] -= int(move[1])
    if move_point == '':
        distance = get_distance(START_POINTS, end_points)
        print ("Then, the output of the program should be: ", round(distance))
        break