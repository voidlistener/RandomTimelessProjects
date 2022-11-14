data = []
from itertools import permutations, combinations

def dist(route):
    ans = 0
    y = 0
    for i in route:
        ans += data[y][i]
        y = i
    return ans
def uq(megaarr):
    d = set()
    for item in megaarr:
            if item in d:
                return False
            d.add(item)
    return True
def uq2(megaarr):
    d = set()
    for item in megaarr:
        for value in item:
            if value in d:
                return False
            d.add(value)
    return True
def arrinmegarr(megarr, arr):
    for i in range(k):
        s = 0
        for item in arr:
            if item in megarr[i]:
                s += 1
        if s == 0:
            return False
    return True
def balance(route):
    b = 0
    for item in route:
        if item <= n:
            b += 1
        else:
            b -= 1
        if b < 0 or b > 25:
            return False
    return True
def megal(megarr):
    l = 0
    for item in megarr:
        for value in item:
            l += 1
    return l
with open("input1.txt") as f:
    n, m, k = list(map(int, f.readline().split()))
    for i in range(n+m+1):
        data.append(list(map(int, f.readline().split())))
    travel = list(map(int, f.readline().split()))
print(n, m ,k)
print("Data complete")
dmx = max(travel)
dmn = min(travel)/2
nodes = [i for i in range(1, n+m)]
routes = []
for i in range(2, 2*min(n//k, m//k)+1, 2):
    print(i)
    for item in permutations(nodes, i):
        if (item[0] <= n) and (item[-1] > n) and uq(item) and balance(item) and (dist(item) <= dmx) and (dist(item) >= dmn):
            routes.append(item)
print("Permutations 1 complete")
cars = []
for i in range(k):
    cars.append([])
    for item in routes:
        if dist(item) <= travel[i]:
            cars[i] += [item]
ult = []
for item in combinations(routes, k):
    if uq2(item) and arrinmegarr(cars, item):
        ult.append(item)
print("Combinations 2 complete")
ult.sort(key = lambda a: megal(a))
final = list(ult[-1])
final.sort(key = lambda a: dist(a))
travel = [[travel[i], i] for i in range(k)]
travel.sort()
for i in range(k):
    travel[i].append(i)
travel.sort(key = lambda a: a[1])
print("Routes chosen")

with open("output1.txt", "w") as f:
    for i in range(k):
        t = travel[i][2]
        s = str(len(final[t]))
        for item in final[t]:
            s += " "
            s += str(item)
        s += "\n"
        f.write(s)