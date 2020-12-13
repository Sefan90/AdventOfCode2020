import time
import math
from functools import reduce
def Part1():
    f = open("input.txt","r")
    inputlist = f.readlines()
    departtime = int(inputlist[0])
    bus = [int(i) for i in inputlist[1].split(",") if i.isnumeric()]
    bustime = 99
    bestbus = 0
    for b in bus:
        temp = math.ceil(departtime/b)*b-departtime
        if bustime > temp and temp >= 0:
            bestbus = b
            bustime = temp
    print(bestbus*bustime)


def find_xy(k, v, i, incr):
    while True:
        if (i+v)%k==0:
            return(i)
        i += incr

def Part2():
    bus_notes = open("input.txt").read().split("\n")
    buss_schedule = (bus_notes[1].split(","))
    summa = {}
    lista = []
    time = 1
    inc = 1
    
    for x in range(len(buss_schedule)):
        if buss_schedule[x] == "x":
            continue
        summa[buss_schedule[x]] = x
        lista.append(int(buss_schedule[x]))

    for k, v in summa.items():
        time = find_xy(int(k) ,v , time, inc)
        inc *= int(k)
    print(time)

Part2()