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
    f = open("input.txt","r")
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
            myticket = [int(i) for i in row.split(",")]
            continue
        elif ":" in row:
            templist = []
            for i in range(int(row.split(":")[1].split()[0].split("-")[0]),int(row.split(":")[1].split()[0].split("-")[1])+1):
                templist.append(i)
            for i in range(int(row.split(":")[1].split()[-1].split("-")[0]),int(row.split(":")[1].split()[-1].split("-")[1])+1):
                templist.append(i)
            rule[row.split(":")[0]] = templist
        else:
            nearbytickets[row] = [int(i) for i in row.split(",")]

    # Removes nearbytickets which aren't valid for any field
    delete = []
    for k,v in nearbytickets.items():
        for i in v:
            found = False
            for _,rv in rule.items():
                if i in rv:
                    found = True
            if found == False:
                delete += [k]
    for d in delete:
        if d in nearbytickets.keys():
            del nearbytickets[d]

    # Creates a dict with all Rules and possibel placements for them
    ruledict = {}
    for rk,rv in rule.items():
        rulelist = []
        for i in range(len(list(nearbytickets.values())[0])):
            found = True
            for key in nearbytickets.keys():
                if nearbytickets.get(key)[i] not in rv:
                    found = False
            if found == True:
                rulelist.append(i)
        ruledict[rk] = rulelist
    
    # Puts the Rules in the correct order
    resultlist = []
    for _ in ruledict.items():
        resultlist.append("")
    while "" in resultlist:
        for k,v in ruledict.items():
            if len(v) == 1:
                resultlist[v[0]] = k
                for rk,rv in ruledict.items():
                    if v[0] in rv and k != rk:
                        rv.remove(v[0])
                        ruledict[rk] = rv
                v = []

    result = 1
    for i, r in enumerate(resultlist):
        if "departure" in r:
            result *= myticket[i]

    print(result)

Part2()