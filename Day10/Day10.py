def Part1():
    f = open("input.txt","r")
    currentsum = 0
    jolt = [0,0,1] #your device's built-in adapter is always 3 higher than the highest adapter
    inputlist = sorted([int(i) for i in f.readlines()])
    for i in inputlist:
        jolt[i - currentsum-1] += 1
        currentsum = i
    print(jolt[0]*jolt[2])

def Part2():
    f = open("input.txt","r")
    inputlist = [0] + sorted([int(i) for i in f.readlines()])
    inputlist.append(max(inputlist)+3)
    result = 1
    counter = 0
    for i in range(len(inputlist)-1):
        if inputlist[i+1] - inputlist[i] == 1:
            counter += 1
        elif inputlist[i+1] - inputlist[i] == 3:
            if counter == 2:
                result *= 2
            elif counter == 3:
                result *= 4
            elif counter == 4:
                result *= 7
            counter = 0
    print(result)

import time
start_time = time.time()
Part2()
print("--- %s seconds ---" % (time.time() - start_time))

