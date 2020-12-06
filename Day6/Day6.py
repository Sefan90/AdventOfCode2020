def Part1():
    f = open("input.txt","r")
    lines = f.readlines()
    yes = [False]*26
    sum = 0
    for i in lines:
        if i in ['\n', '\r\n']:
            sum += yes.count(True);
            yes = [False]*26
            continue
        else:
            for l in i:
                if l != '\n':
                    yes[ord(l)-97] = True
    sum += yes.count(True);
    print(sum)

def Part2():
    f = open("input.txt","r")
    lines = f.readlines()
    yes = [True]*26
    sum = 0
    for i in lines:
        if i in ['\n', '\r\n']:
            sum += yes.count(True);
            yes = [True]*26
            continue
        else:
            for l in range(len(yes)):
                if chr(l+97) not in i:
                    yes[l] = False
    sum += yes.count(True);
    print(sum)

import time
start_time = time.time()
Part2()
print("--- %s seconds ---" % (time.time() - start_time))