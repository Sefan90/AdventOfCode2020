def rec(i,row):
    summa = 0
    lastitem = ""
    while i < len(row):
        lastitem += row[i]
        if ")" in lastitem:
            return summa, i
        elif "(" in lastitem:
            tmp, i = rec(i+1,row)
            if summa == 0:
                summa = tmp
            elif lastitem[0] == '+':
                summa += tmp
            else:
                summa *= tmp
            lastitem = "" #lastitem[:-2]
        elif summa == 0: #and row[i].isnumeric() #and len(lastitem) <= 1: #Kanske fel
            summa = int(row[i])
            lastitem = ""
        else:
            if len(lastitem) == 2:
                if lastitem[0] == '+':
                    summa += int(lastitem[1])
                else:
                    summa *= int(lastitem[1])
                lastitem = ""
        i += 1
    return summa, i

def Part1():
    f = open("input.txt","r")
    inputlist = [[i for i in r.replace(" ","").strip()] for r in f.readlines()]
    summa = 0
    for row in inputlist:
        tmp, _ = rec(0,row)
        summa += tmp
        #print(tmp)
        
    #print(inputlist)
    print(summa)

Part1()