def func(lista):
    while len(lista) > 1:
        while "+" in lista:
            for l, listitem in enumerate(lista):
                if listitem == "+":
                  tmp = eval(' '.join(map(str, lista[l-1:l+2])))
                  del lista[l-1:l+2]
                  lista.insert(l-1,str(tmp))
                  break
        while "*" in lista:
            for l, listitem in enumerate(lista):
                if listitem == "*":
                  tmp = eval(' '.join(map(str, lista[l-1:l+2])))
                  del lista[l-1:l+2]
                  lista.insert(l-1,str(tmp))
                  break
    return int(lista[0])

def Part2():
    f = open("testinput.txt","r")
    inputlist = [[i for i in r.replace(" ","").strip()] for r in f.readlines()]
    print(inputlist)
    summa = 0
    for row in inputlist:
        while "(" in row:
            count = 0
            for i, item in enumerate(row):
                if item == "(":
                    if count == 0:
                        start1 = i
                        count += 1
                    elif count == 1:
                        start2 = i
                        count += 1
                elif item == ")":
                    if count == 2:
                        end2 = i
                        tmp = func([r for r in row[start2+1:end2]])
                        del row[start2:end2+1]
                        row.insert(start2,str(tmp))
                        count -= 1
                        break
                    elif count == 1:
                        end1 = i
                        tmp = func([r for r in row[start1+1:end1]])
                        del row[start1:end1+1]
                        row.insert(start1,str(tmp))
                        count -= 1
                        break
        summa += func(row)
    print(summa)

Part2()