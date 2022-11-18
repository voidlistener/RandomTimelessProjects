x_size = 59
y_size = 31

tile_size = 1
wall_size = 0.1

import random

def value_check(r, value):
    ans = False
    for item in r:
        if item.count(value):
            ans = True
    return ans

def nearby_check(x0, y0, r, value):
    return (r[y0-1][x0] == value or r[y0+1][x0] == value or r[y0][x0-1] == value or r[y0][x0+1] == value)


def carve(x0 ,y0, r):
    r[y0][x0] = 0
    if y0 > 0 and r[y0-1][x0] == 8:
        r[y0-1][x0] = random.randint(0, 1)
        if r[y0-1][x0] == 0:
            carve(x0, y0-1, r)
    if y0 < y_size-1 and r[y0+1][x0] == 8:
        r[y0+1][x0] = random.randint(0, 1)
        if r[y0+1][x0] == 0:
            carve(x0, y0+1, r)
    if x0 > 0 and r[y0][x0-1] == 8:
        r[y0][x0-1] = random.randint(0, 1)
        if r[y0][x0-1] == 0:
            carve(x0-1, y0, r)
    if x0 < x_size-1 and r[y0][x0+1] == 8:
        r[y0][x0+1] = random.randint(0, 1)
        if r[y0][x0+1] == 0:
            carve(x0+1, y0, r)
def display(r):
    for y in range(y_size):
        for x in range(x_size):
            print(r[y][x], end="")
        print("")

def main():
    room = [[8 for i in range(x_size)] for j in range(y_size)]
    for y in range(y_size):
        for x in range(x_size):
            if y % (y_size-1) == 0 or x % (x_size-1) == 0:
                room[y][x] = 1
    x_t = random.randint(1, x_size-2)
    y_t = random.randint(1, y_size-2)
    carve(x_t, y_t, room)
    while value_check(room, 8):
        x_t = random.randint(1, x_size-2)
        y_t = random.randint(1, y_size-2)
        if room[y_t][x_t] == 1 and nearby_check(x_t, y_t, room, 8) and nearby_check(x_t, y_t, room, 0):
            carve(x_t, y_t, room)
    for y in range(y_size):
        for x in range(x_size):
            if room[y][x] == 1:
                room[y][x] = "█"
            if room[y][x] == 0:
                room[y][x] = " "
    display(room)
main()