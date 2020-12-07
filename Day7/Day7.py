myset = set()
def rec1(baglist,currentbag):
    for bag, contain in baglist.items():
        if "shiny gold bag" in currentbag:
            return True
        elif currentbag in bag:
            for c in contain:
                tmp = rec1(baglist,c[3:].strip().replace(".",""))
                if tmp == True:
                    myset.add(currentbag.strip().replace("bags","bag"))
                    return True
    return False

def Part1():
    f = open("input.txt","r")
    lines = f.readlines()
    baglist = {}
    for i in lines:
        baglist[i.split("contain")[0]] = i.split("contain")[1].split(",")
    for bag, _ in baglist.items(): 
        tmp = rec1(baglist,bag) 
        if tmp == True:
            myset.add(bag.strip().replace("bags","bag"))
    myset.remove("shiny gold bag")
    print(myset)
    print(len(myset))

def rec2(baglist,currentbag,bagcount,counter):
    for bag, contain in baglist.items():
        if currentbag in bag:
            for c in contain:
                if c[:3].strip() != 'no':
                    counter += bagcount * int(c[:3].strip())
                    counter = rec2(baglist,c[3:].strip().replace(".",""),bagcount * int(c[:3].strip()),counter)
    return counter

def Part2():
    f = open("input.txt","r")
    lines = f.readlines()
    baglist = {}
    counter = 0
    for i in lines:
        baglist[i.split("contain")[0]] = i.split("contain")[1].split(",")
    counter =rec2(baglist,"shiny gold bag",1,counter) 
    print(counter)

import time
start_time = time.time()
Part2()
print("--- %s seconds ---" % (time.time() - start_time))