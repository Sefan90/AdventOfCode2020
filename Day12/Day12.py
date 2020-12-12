def Part1():
    f = open("input.txt","r")
    inputlist = f.readlines()
    facing = 90
    pos = [0,0]
    for i in inputlist:
        print(i)
        if i[0] == "W":
            pos[0] -= int(i[1:])
        elif i[0] == "E":
            pos[0] += int(i[1:])
        elif i[0] == "S":
            pos[1] += int(i[1:])
        elif i[0] == "N":
            pos[1] -= int(i[1:])
        elif i[0] == "R":
            facing = (facing+int(i[1:]))%360
        elif i[0] == "L":
            facing = (facing-int(i[1:]))%360
        elif i[0] == "F":
            if facing == 0:
                pos[0] -= int(i[1:])
            elif facing == 90:
                pos[0] += int(i[1:])
            elif facing == 180:
                pos[1] += int(i[1:])
            elif facing == 270:
                pos[1] -= int(i[1:])
        print(pos)
    print(abs(pos[0])+abs(pos[1]))

def Part2():
    f = open("input.txt","r")
    inputlist = f.readlines()
    pos = [0,0,0,0]
    waypoint = [1,10,0,0]
    for i in inputlist:
        if i[0] == "N":
            waypoint[0] += int(i[1:])
        elif i[0] == "E":
            waypoint[1] += int(i[1:])
        elif i[0] == "S":
            waypoint[2] += int(i[1:])
        elif i[0] == "W":
            waypoint[3] += int(i[1:])
        elif i[0] == "R":
            for w in range(int(int(i[1:])/90)):
                temp = waypoint[0]
                waypoint[0] = waypoint[3]
                waypoint[3] = waypoint[2]
                waypoint[2] = waypoint[1]
                waypoint[1] = temp
        elif i[0] == "L":
            for w in range(int(int(i[1:])/90)):
                temp = waypoint[0]
                waypoint[0] = waypoint[1]
                waypoint[1] = waypoint[2]
                waypoint[2] = waypoint[3]
                waypoint[3] = temp
        elif i[0] == "F":
            for w in range(len(waypoint)):
                pos[w] += int(i[1:])*waypoint[w]
    print(abs(pos[0]-pos[2])+abs(pos[1]-pos[3]))

import time
start_time = time.time()
Part2()
print("--- %s seconds ---" % (time.time() - start_time))

