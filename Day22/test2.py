


def func(lista):
    while len(lista) > 1:
        while "+" in lista:
            for i, item in enumerate(lista):
                if item == "+":
                  tmp = eval(' '.join(map(str, lista[i-1:i+2])))
                  del lista[i-1:i+2]
                  lista.insert(i-1,str(tmp))
                  break
        while "*" in lista:
            for i, item in enumerate(lista):
                if item == "*":
                  tmp = eval(' '.join(map(str, lista[i-1:i+2])))
                  del lista[i-1:i+2]
                  lista.insert(i-1,str(tmp))
                  break
    return int(lista[0])

def decoupler(line):
    while "(" in line:
        count = 0
        for x, n in enumerate(line):
            if (n == "(" and count == 0):
                start = x
                count += 1
            elif n == "(" and count == 1:
                start_2 = x
                count += 1
            elif n == ")" and count == 2:
                end_2 = x
                tmp = func([i for i in line[start_2 + 1:end_2]])
                del line[start_2:end_2 + 1]
                line.insert(start_2, str(tmp))
                count -= 1
                break
            elif n == ")" and count == 1:
                end = x
                #Replace our () with a sum in the list
                tmp = func([i for i in line[start + 1:end]])
                del line[start:end + 1]
                line.insert(start, str(tmp))
                count -= 1
                break
    print(line)
    return(line)

def Part2():
    f = open("testinput.txt","r")
    inputlist = [[i for i in r.replace(" ","").strip()] for r in f.readlines()]
    print(inputlist)
    start1 = None
    start2 = None
    end1 = None
    end2 = None
    summa = 0
    for row in inputlist:
        while "(" in row:
            count = 0
            for i, item in enumerate(row):
                print(i)
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
                        tmp = func([r for r in range(start2+1,end2)])
                        del row[start2:end2+1]
                        row.insert(start2,str(tmp))
                        count -= 1
                        break
                    elif count == 1:
                        end1 = i
                        tmp = func([r for r in range(start1+1,end1)])
                        del row[start1:end1+1]
                        row.insert(start1,str(tmp))
                        count -= 1
                        break
        summa += func(row)
    print(summa)

Part2()