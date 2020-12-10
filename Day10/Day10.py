import itertools
import math
def Part1():
    f = open("input.txt","r")
    currentsum = 0
    jolt = [0,0,1] #your device's built-in adapter is always 3 higher than the highest adapter
    inputlist = sorted([int(i) for i in f.readlines()])
    for i in inputlist:
        jolt[i - currentsum-1] += 1
        currentsum = i
    print(jolt[0]*jolt[2])

def Connect(inputlist):
    currentsum = 0
    jolt = [0,0,1] #your device's built-in adapter is always 3 higher than the highest adapter
    for i in inputlist:
        if i - currentsum-1 in [0,1,2]:
            jolt[i - currentsum-1] += 1
            currentsum = i
        else:
            return -1
    return currentsum

def Part2():
    f = open("input.txt","r")
    result =[]
    inputlist = sorted([int(i) for i in f.readlines()])
    maxlist = max(inputlist)
    for i in range(math.floor(maxlist/3),len(inputlist)+1):
        for subset in itertools.combinations(inputlist, i):
            print(subset)
            if max((abs(x - y) for (x, y) in zip(subset[1:], subset[:-1])), default=4) < 4 and min(subset, default = 4) < 4 and max(subset, default = 0) == maxlist:
                result.append(19)
    print(result.count(maxlist)) 


import time
start_time = time.time()
Part2()
print("--- %s seconds ---" % (time.time() - start_time))

