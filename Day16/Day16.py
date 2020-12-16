def Part1():
    f = open("input.txt","r")
    inputlist = f.readlines()
    rule = []
    nearbytickets = []
    for row in inputlist:
        if row in  ["your ticket:\n","nearby tickets:\n","\n"]:
            continue
        elif ":" in row:
            for i in range(int(row.split(":")[1].split()[0].split("-")[0]),int(row.split(":")[1].split()[0].split("-")[1])+1):
                rule.append(i)
            for i in range(int(row.split(":")[1].split()[-1].split("-")[0]),int(row.split(":")[1].split()[-1].split("-")[1])+1):
                rule.append(i)
        else:
            nearbytickets += [int(i) for i in row.split(",")]

    result = 0
    for t in nearbytickets:
        if t not in rule:
            result += t
    print(result)

def Part2():
    f = open("testinput.txt","r")
    inputlist = f.readlines()
    prev = ""
    rule = {}
    myticket = []
    nearbytickets = {}
    for row in inputlist:
        if row in  ["your ticket:\n","nearby tickets:\n", "\n"]:
            prev = row
            continue
        elif prev == "your ticket:\n":
            myticket = [i.replace("\n","") for i in row.split(",")]
            continue
        elif ":" in row:
            rule[row.split(":")[0]] = [row.split(":")[1].split()[0].split("-")[0],row.split(":")[1].split()[0].split("-")[1],row.split(":")[1].split()[-1].split("-")[0],row.split(":")[1].split()[-1].split("-")[1]]
        else:
            nearbytickets[row] = [int(i) for i in row.split(",")]

    delete = []
    for k,v in nearbytickets.items():
        for i in v:
            if i not in rule:
                delete += [k]
                break
    for d in delete:
        del nearbytickets[d]

    result = 0
    print(myticket)
    print(nearbytickets)
    print(rule)

Part2()