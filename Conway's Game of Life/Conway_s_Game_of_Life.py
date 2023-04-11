import random, time, os
WIDTH , HEIGHT = 110, 30

field = []
m ={0: ' ', 1: '◘'}

for y in range(HEIGHT):
    field.append([])
    for x in range(WIDTH):
        field[y].append(random.randint(0, 1))

while True:
    os.system('cls') 
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(m[field[y][x]], end = '')
        print()

    for y in range(HEIGHT):
        for x in range(WIDTH):

            state = field[y][x] % 10
            team = 0

            up = y-1
            down = y+1
            left = x-1
            right = x+1
            
            if up > -1:
                if field[up][x] % 10 == 1:
                    team += 1
                if left > -1:
                    if field[up][left] % 10 == 1:
                        team += 1
            if right < WIDTH-1:
                if field[y][right] % 10 == 1:
                    team += 1
                if up > -1:
                    if field[up][right] % 10 == 1:
                        team += 1
            if down < HEIGHT-1:
                if field[down][x] % 10 == 1:
                    team += 1
                if right < WIDTH-1:
                    if field[down][right] % 10 == 1:
                        team += 1
            if left > -1:
                if field[y][left] % 10 == 1:
                    team += 1
                if down < HEIGHT-1:
                    if field[down][left] % 10 == 1:
                        team += 1
            
            

            if team == 3 or (state == 1 and team == 2):
                field[y][x] += 10


    for y in range(HEIGHT):
        for x in range(WIDTH):
            if field[y][x] >= 10:
                field[y][x] = 1
            else:
                field[y][x] = 0

    time.sleep(0.25)
