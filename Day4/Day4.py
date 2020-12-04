def Part1():
    f = open("input.txt","r")
    lines = f.readlines()
    counter = 0
    check = ["byr","iyr","eyr","hgt","hcl","ecl","pid"] # cid is optional
    found = [False,False,False,False,False,False,False]
    for i in lines:
        if i in ['\n', '\r\n']:
            found = [False,False,False,False,False,False,False]
            continue
        else:
            for items in i.split():
                keyvalue = items.split(":")
                for c in range(len(check)):
                    if keyvalue[0] == check[c]:
                        found[c] = True
        if all([f == True for f in found]):
            counter += 1
            found = [False,False,False,False,False,False,False]
    print(counter)

def Part2():
    f = open("input.txt","r")
    lines = f.readlines()
    counter = 0
    check = ["byr","iyr","eyr","hgt","hcl","ecl","pid"] # cid is optional
    found = [False,False,False,False,False,False,False]
    for i in lines:
        if i in ['\n', '\r\n']:
            found = [False,False,False,False,False,False,False]
            continue
        else:
            for items in i.split():
                keyvalue = items.split(":")
                if keyvalue[0] == check[0] and int(keyvalue[1]) >= 1920 and int(keyvalue[1]) <= 2002:
                    found[0] = True
                elif keyvalue[0] == check[1] and int(keyvalue[1]) >= 2010 and int(keyvalue[1]) <= 2020:
                    found[1] = True
                elif keyvalue[0] == check[2] and int(keyvalue[1]) >= 2020 and int(keyvalue[1]) <= 2030:
                    found[2] = True
                elif keyvalue[0] == check[3] and "in" in keyvalue[1]:
                    if int(keyvalue[1].replace("in","")) >= 59 and int(keyvalue[1].replace("in","")) <= 76:
                        found[3] = True
                elif keyvalue[0] == check[3] and "cm" in keyvalue[1]:
                    if int(keyvalue[1].replace("cm","")) >= 150 and int(keyvalue[1].replace("cm","")) <= 193:
                        found[3] = True
                elif keyvalue[0] == check[4] and keyvalue[1][:1] == "#" and len(keyvalue[1]) == 7 and int(keyvalue[1][1:],16): #Dålig check
                    found[4] = True
                elif keyvalue[0] == check[5] and keyvalue[1] in {"amb","blu","brn","gry","grn","hzl","oth"}:
                    found[5] = True
                elif keyvalue[0] == check[6] and len(keyvalue[1]) == 9 and keyvalue[1].isnumeric():
                    found[6] = True
        if all([f == True for f in found]):
            counter += 1
            found = [False,False,False,False,False,False,False]
    print(counter)

Part2()