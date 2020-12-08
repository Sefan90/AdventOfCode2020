def console(counter,oplist,rownr):
    lastelement = False
    if rownr < len(oplist):
        row = oplist[rownr].split()
        if row[0] == "nop":
            oplist[rownr] = "exit 0"
            counter, lastelement = console(counter,oplist,rownr+1)
        elif row[0] == "acc":
            oplist[rownr] = "exit 0"
            counter, lastelement = console(counter+int(row[1]),oplist,rownr+1)
        elif row[0] == "jmp":
            oplist[rownr] = "exit 0"
            counter, lastelement = console(counter,oplist,rownr+int(row[1]))
        return counter, lastelement
    return counter, True

def Part1():
    f = open("input.txt","r")
    oplist = f.readlines()
    counter = 0
    print(console(counter,oplist,0)[0])

def Part2():
    f = open("input.txt","r")
    oplist = f.readlines()
    for i in range(len(oplist)):
        newlist = oplist.copy()
        if "nop" in newlist[i]:
            newlist[i] = "jmp "+ newlist[i].split()[1]
        elif "jmp" in newlist[i]:
            newlist[i] = "nop "+ newlist[i].split()[1]
        else:
            continue
        counter, lastelement = console(0,newlist,0)
        if lastelement == True:
            print(counter)
            break

import time
start_time = time.time()
Part2()
print("--- %s seconds ---" % (time.time() - start_time))