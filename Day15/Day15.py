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

Part1()