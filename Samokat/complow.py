from math import floor

data = []
with open("input25.txt") as f:
    n, m, k = list(map(int, f.readline().split()))
    for i in range(n+m+1):
        data.append(list(map(int, f.readline().split())))
    travel = list(map(int, f.readline().split()))
def dist(route):
    ans = 0
    y = 0
    for i in route:
        ans += data[y][i]
        y = i
    return ans
def b_subroute(route, a, b):
    bl = 0
    state1 = 1 if route[a] <= n else -1
    state2 = 1 if route[b] <= n else -1 
    for i in range(b):
        if route[i] <= n:
            bl += 1
        else:
            bl -= 1
        ans = bl - state1+state2
        if i >= a and (ans < 0 or ans > 25):
            return False
    return True
def stabilize(route):
    l = len(route)
    b = 0
    for i in range(l):
        if route[i] <= n:
            b += 1
        else:
            b -= 1
        if b == -1:
            for j in range(i, l):
                if route[j] <= n:
                    t = route[i]
                    route[i] = route[j]
                    route[j] = t
                    b = 1
                    break
        if b == 26:
            for j in range(i, l):
                if route[j] > n:
                    t = route[i]
                    route[i] = route[j]
                    route[j] = t
                    b = 24
                    break
def optimize(route):
    l = len(route)
    for i in range(l-1):
        for j in range(i+1, l):
            a11, b11 = data[0][route[i]], data[0][route[j]]
            a22, b22 = 0, 0
            a12, a21, b12, b21 = data[route[i]][route[i+1]], data[route[j-1]][route[j]], data[route[j]][route[i+1]], data[route[j-1]][route[i]]
            if j == i+1:
                a12, a21, b12, b21 = 0, data[route[i]][route[j]], 0, data[route[j]][route[i]]
            if i > 0:
                a11, b11 = data[route[i-1]][route[i]], data[route[i-1]][route[j]]
            if j < l-1:
                a22, b22 = data[route[j]][route[j+1]], data[route[i]][route[j+1]]
            if (a11 + a12 + a21 + a22) > (b11 + b12 + b21 + b22):
                if b_subroute(route, i, j):
                    t = route[i]
                    route[i] = route[j]
                    route[j] = t


                
def opt_loop(route):
    change = True
    while change:
        tdist = dist(route)
        #print(tdist)
        optimize(route)
        if tdist == dist(route):
            change = False

def besties_sort(arr, friends, type = "g"):
    if type == "d":
        for i in range(len(arr)):
            l = len(friends)
            for j in range(l):
                if arr[i][0] == friends[j]:
                    arr[i][1] = 0
                    if arr[i][0] == 0:
                        if j == 0:
                            arr[i][1] += data[0][friends[j]]
                        else:
                            arr[i][1] += data[friends[j-1]][friends[j]]
                    if j < l-1:
                        arr[i][1] += data[friends[j]][friends[j+1]] 
                    break

    for i in range(len(arr)):
        s = 0
        for friend in friends:
            s += min(data[arr[i][0]][friend], data[friend][arr[i][0]])
        if type == "d":
            arr[i][1] += s
        else:
            arr[i][1] = s
    arr.sort(key = lambda a: a[1])

def cut_route(route):
    #l = len(route)
    #a = 0
    #b = l-1
    #mxin = data[0][route[0]]
    #mxout = data[route[l-2]][route[l-1]]
    #for i in range(1, l-1):
    #    d = data[route[i-1]][route[i]]+data[route[i]][route[i+1]]
    #    if route[i] <= n and d >= mxin:
    #        a = i
    #        mxin = d
    #    if route[i] > n and d >= mxout:
    #        b = i
    #        mxout = d
    #route.pop(max(a, b))
    #route.pop(min(a, b))

    h_ins, h_outs = [], []

    for item in route:
        if item <= n:
            h_ins.append([item, 0])
        else:
            h_outs.append([item, 0])
    besties_sort(h_ins, route, type = "d")
    route.remove(h_ins[-1][0])
    besties_sort(h_outs, route, type = "d")
    route.remove(h_outs[-1][0])

def upd_avg(nodes):
    new_ins = []
    new_outs = []
    for item1 in nodes:
        v = 0
        kv = 0
        h = 0
        kh = 0
        for item2 in nodes:
            if item1 != item2:
                v += data[item2][item1]
                kv += 1
                h += data[item1][item2]
                kh += 1
        res = [item1, v/kv + h/kh]
        if item1 <= n:
            new_ins.append(res)
        else:
            new_outs.append(res)
    new_ins.sort(key = lambda a: a[1])
    new_outs.sort(key = lambda a: a[1])
    return new_ins, new_outs


    




print(n, m ,k)
print("Data complete")
avg_ins, avg_outs = [], []
nodes = [i for i in range(1, n+m+1)]

for i in range(1, n+m+1):
    v = 0
    kv = 0
    h = 0
    kh = 0
    for j in range(n+m+1):
        if i != j:
            if not(i > n and j == 0):
                v += data[j][i]
                kv += 1
            if j != 0:
                h += data[i][j]
                kh += 1
    res = [i, v/kv + h/kh]
    if i <= n:
        avg_ins.append(res)
    else:
        avg_outs.append(res)
avg_ins.sort(key = lambda a: a[1])
avg_outs.sort(key = lambda a: a[1])
print("Averages complete")
fuel = sum(travel)
travel = [[travel[i], i] for i in range(k)]
travel.sort()
travel.reverse()
mv = min(n, m)
tree = [2*floor(mv * (travel[i][0]/fuel)) for i in range(k)]
print(tree)
cars = [[] for i in range(k)]
for i in range(k):
    s = 0
    while s < tree[i]:
        nin = avg_ins[0][0]
        cars[i].append(nin)
        nodes.remove(nin)
        avg_ins.pop(0)
        besties_sort(avg_outs, cars[i])
        nout = avg_outs[0][0]
        cars[i].append(nout)
        nodes.remove(nout)
        avg_outs.pop(0)
        besties_sort(avg_ins, cars[i])
        
        s += 2
    avg_ins, avg_outs = upd_avg(nodes)
for car in cars:
    opt_loop(car)
    print("Car optimized")
print("Optims complete")
answer = []
for i in range(k):
    for j in range(len(cars)):
        while dist(cars[j]) > travel[i][0]:
            cut_route(cars[j])
            stabilize(cars[j])
            opt_loop(cars[j])
    cars.sort(key = lambda a: len(a))
    cars.reverse()
    answer.append(cars[0])
    cars.pop(0)
    print("Car cut")
print("Cuts complete")
for i in range(k):
    

    travel[i].append(i)
travel.sort(key = lambda a: a[1])
print("Routes chosen")

with open("output25.txt", "w") as f:
    for i in range(k):
        t = travel[i][2]
        s = str(len(answer[t]))
        for item in answer[t]:
            s += " "
            s += str(item)
        s += "\n"
        print(s)
        f.write(s)