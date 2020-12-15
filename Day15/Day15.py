import itertools
import copy

def rindex(mylist, myvalue):
    return len(mylist) - mylist[::-1].index(myvalue) - 1


def Part1():
    f = open("input.txt","r")
    inputlist = f.readlines()
    lista = [int(c) for c in [i.split(",") for i in inputlist][0]]
    for i in range(len(lista),30000000):
        lastnr = lista[i-1]
        #print(lastnr)
        if lista.count(lastnr) == 1:
            lista.append(0)
        else:
            poslastnr = rindex(lista,lastnr)
            posdiff = poslastnr - (rindex(lista[:poslastnr],lastnr))
            lista.append(posdiff)
    print(lista[-1])

def Part2():
    f = open("input.txt","r")
    inputlist = f.readlines()
    lista = [int(c) for c in [i.split(",") for i in inputlist][0]]
    count = {}
    pos1 = {}
    pos2 = {}
    lastnr = lista[-1]
    for i in range(len(lista)):
        count[lista[i]] = 1
        pos1[lista[i]] = i
    for i in range(len(lista),30000000):
        if count[lastnr] == 1:
            lastnr = 0
        else:
            lastnr = pos1[lastnr] - pos2[lastnr]
        if lastnr in count.keys():
            count[lastnr] += 1
        else:
            count[lastnr] = 1
        pos2[lastnr] = pos1.get(lastnr)
        pos1[lastnr] = i
    print(lastnr)

Part2()