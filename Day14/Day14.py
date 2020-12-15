import itertools
import copy

def Part1():
    f = open("input.txt","r")
    inputlist = f.readlines()
    mem = {}
    mask = ""
    for i in inputlist:
        if "mask" in i:
            mask = i.split()[2]
        else:
            key = str(i.split("[")[1].split("]")[0])
            value = int(i.split("=")[1].strip())
            binvalue = [v for v in "{:036b}".format(value)]
            for m in range(len(mask)):
                if mask[m] != "X":
                    binvalue[m] = mask[m]
            mem[key] = "".join([str(b) for b in binvalue])         
    result = 0
    for _,v in mem.items():
        result += int(v,2)
    print(result)

def Part2():
    f = open("input.txt","r")
    inputlist = f.readlines()
    mem = {}
    mask = ""
    for i in inputlist:
        if "mask" in i:
            mask = [i for i in i.split()[2]]
        else:
            key = str(i.split("[")[1].split("]")[0])
            value = int(i.split("=")[1].strip())
            binvalue = [v for v in "{:036b}".format(int(key))]
            foundx = []
            ones = 0
            for m in range(len(mask)):
                if  mask[m] == "X":
                    foundx.append(2**(len(mask)-m-1))
                elif mask[m] == "1":
                    ones += 2**(len(mask)-m-1)
                elif binvalue[m] == "1":
                    ones += 2**(len(binvalue)-m-1)
            if not foundx:
                mem[key] = value
            else:
                combi = []
                for fo in range(1,len(foundx)+1):
                    combi += [sum(x) for x in itertools.combinations(foundx, fo)]
                mem[str(ones)] = value
                for c in range(len(combi)):
                    mem[str(combi[c]+ones)] = value
    result = 0
    for _,v in mem.items():
        result += v
    print(result)
    #3380819073794 Fel

Part2()