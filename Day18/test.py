import copy
import re
def Part1():
    f = open("testinput.txt","r")
    inputlist = [[i for i in r.replace(" ","").strip()] for r in f.readlines()]
    for row in inputlist:
        newlist = []
        for i in range(len(row)):
            #print(row[i])
            if row[i] == "+":
                newlist.append(str(int(row[i-1])+int(row[i+1])))
            elif row[i] == "*":
                newlist.append("*")
        print(newlist)
        summa = 1
        for i in range(len(newlist)):
            if newlist[i].isnumeric():
                summa *= int(newlist[i])
        print(summa)

def rec2(row):
    newlist = []
    for i in range(len(row)):
        if row[i] == "+":
            newlist.append(str(int(row[i-1])+int(row[i+1])))
        elif row[i] == "*":
            newlist.append(str(int(row[i-1])*int(row[i+1])))
    return newlist

def rec(row):
    newlist = []
    for i in range(len(row)):
            #print(row[i])
        if len(row[i]) > 1:
            newlist += rec(row[i])
        elif row[i] == "+":
            newlist.append(str(int(row[i-1])+int(row[i+1])))
        elif row[i] == "*":
            newlist.append("*")
    return newlist
            

def splitstr(my_string):
    in_parens=False
    buffer=''
    my_list = []
    for char in my_string:
        if char == ' ':
            continue
        if char =='(':
            in_parens=True
        elif char==')':
            in_parens = False
            my_list.append(buffer)
            buffer=''
        elif in_parens:
            buffer+=char
        else:
            my_list.append(char)
    return my_list

def par():
    f = open("testinput.txt","r")
    inputlist = [[i for i in splitstr(r.strip())] for r in f.readlines()]
    print(inputlist)
    for row in inputlist:
        lista = []
        for i in row:
            if len(i) > 1:
                lista += rec(i)
            else:
                lista.append(i)
        print(lista)
    for row in inputlist:
        newlist = rec(row)
        print(newlist)
        summa = 1
        for i in range(len(newlist)):
            if newlist[i].isnumeric():
                summa *= int(newlist[i])
        print(summa)


def par2():
    f = open("testinput.txt","r")
    inputlist = [[i for i in r.replace(" ","").strip()] for r in f.readlines()]
    print(inputlist)
    newlist = []
    para = 0
    for k,row in enumerate(inputlist):
        while True:
            lista = []
            for i in row:
                if i == "(":
                    para += 1
                elif i == ")":
                    para -= 1
                elif para == 0:
                    if len(lista) == 0:
                        newlist.append(i)
                    else:
                        lista.append(i)
                        newlist.append([lista])
                        lista = []
            inputlist[k] = copy.deepcopy(newlist)
            if "(" not in newlist:
                break
    print(inputlist)



par()