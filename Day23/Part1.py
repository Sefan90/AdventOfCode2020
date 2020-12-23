def cupstomove(cups,currentindex):
    #cups[currentindex+1:currentindex+4]
    tmp = []
    for i in range(currentindex+1,currentindex+4):
        if i >= len(cups):
            tmp.append(cups[i-len(cups)])
        else:
            tmp.append(cups[i])
    return tmp

def findnewcup(cups,currentcup):
    for c in range(1,len(cups)):
        tmp = currentcup - c
        if tmp < 1:
            tmp += max(cups)
        if tmp in cups:
            currentcup = tmp
            currentindex = cups.index(currentcup)
            break
    return currentindex

def part1():
    file = open("input.txt","r").readlines()
    cups = [[int(item) for item in row] for row in file][0]
    currentcup = cups[0]
    currentindex = 0
    #print(cups)
    #print(cups[:currentindex+1] + cups[currentindex+currentcup+1:])
    #print(cups[currentindex+1:currentindex+currentcup+1])
    for _ in range(100):
        #print(cups)
        cupsmoved = cupstomove(cups,currentindex)
        tmplist = [c for c in cups if c not in cupsmoved]
        #print(cupsmoved)
        newpos = findnewcup(tmplist,currentcup)
        cups = tmplist[:newpos+1] + cupsmoved + tmplist[newpos+1:]
        newpos = cups.index(currentcup)
        if newpos != currentindex:
            cups = cups[newpos-currentindex:] + cups[:newpos-currentindex]
        currentindex = (currentindex+1)%len(cups)
        #print(currentindex)
        currentcup = cups[currentindex]
    
    cups = cups[cups.index(1)+1:] + cups[:cups.index(1)]
    output = ""
    for c in cups:
        output += str(c)
    print(output)
    
part1()