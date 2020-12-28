import sys
import copy
from functools import lru_cache
#print(sys.getrecursionlimit())
sys.setrecursionlimit(3000)
#print(sys.getrecursionlimit())
file = open("input.txt","r").readlines()
ruledict = {r[:r.index(":")]:[i for i in r[r.index(":")+1:].replace(' ',"").replace('"',"").strip()] for r in file if ":" in r}
messagelist = [r.strip() for r in file if ":" not in r][1:]
numberlist = [str(i) for i in range(10)]

def rec(wordlist,i):
    newlist = []
    if i == 0:
        newlist = ruledict.get(wordlist[i]) + wordlist[i+1:]
    elif i >= len(wordlist):
        newlist = wordlist[:i] + ruledict.get(wordlist[i])
    else:
        newlist = wordlist[:i] + ruledict.get(wordlist[i]) + wordlist[i+1:]
    if any(w in numberlist for w in newlist):
        if newlist[i] in numberlist:
            newlist,i = rec(newlist,i)
        else:
            newlist,i = rec(newlist,i+1)
    return newlist,i

@lru_cache(maxsize=10000)
def rec2(wordlist):
    newlist = [""]
    wordlist = list(wordlist)
    for item in wordlist:
        if ruledict.get(item)[0] in ["a","b"]:
            for i in range(len(newlist)):
                newlist[i] += ruledict.get(item)[0]
        else:
            if "|" in ruledict.get(item):
                index = ruledict.get(item).index("|")
                item1 = ruledict.get(item)[:index]
                item2 = ruledict.get(item)[index+1:]
                tmplist = []
                for i in range(len(newlist)):
                    tmp1 = rec2(tuple(item1))
                    tmp2 = rec2(tuple(item2))
                    for t in range(len(tmp1)):
                        tmplist.append(newlist[i]+tmp1[t])
                    for t in range(len(tmp2)):
                        if t == len(tmp2)-1:
                            newlist[i] += tmp2[t]
                        else:
                            tmplist.append(newlist[i]+tmp2[t])
                newlist += tmplist
            else:
                tmplist = []
                for i in range(len(newlist)):
                    tmp = rec2(tuple(ruledict.get(item)))
                    for t in range(len(tmp)):
                        if t == len(tmp)-1:
                            newlist[i] += tmp[t]
                        else:
                            tmplist.append(newlist[i]+tmp[t])
                newlist += tmplist
    return newlist

@lru_cache(maxsize=200)
def rec3(item):
    newlist = []
    if item in ["a","b"]:
        newlist = item
    elif ruledict.get(item)[0] in ["a","b"]:
        newlist = ruledict.get(item)[0]      
    else:
        newlist = ruledict.get(item)
    return newlist

def Part1():
    wordlist = [ruledict.get("0")]
    summa = 0
    tmp = []
    for i in wordlist:
        tmp += rec2(tuple(i))
        
    for i in tmp:
        summa += messagelist.count(i)
    print(summa)

def stillnumber(wordlist):
    for w in wordlist:
        for c in w:
            if c in numberlist:
                return True 
    return False

def Part11():
    wordlist = [ruledict.get("0")]
    summa = 0

    while stillnumber(wordlist):
        newlist = []
        for word in wordlist:
            for item in word:
                if item in ["a","b"]:
                    newlist.append(item)
                    continue
                elif "|" in ruledict.get(item):
                    index = ruledict.get(item).index("|")
                    item1 = ruledict.get(item)[:index]
                    item2 = ruledict.get(item)[index+1:]
                    tmplist = []
                    for i in range(len(newlist)):
                        tmplist.append(newlist[i]+str(item1))
                        newlist[i] += str(item2)
                    newlist += tmplist  
                else:
                    newlist.append(ruledict.get(item)[0])
        wordlist = copy.deepcopy(newlist)
    print(wordlist)
    for i in wordlist:
        summa += messagelist.count(i)
    print(summa)

@lru_cache(maxsize=200)
def Part111():
    wordlist = [ruledict.get("0")]
    summa = 0
    for w, word in enumerate(wordlist):
        while stillnumber(word):
            newlist = []
            for i, item in enumerate(word):
                tmp = rec3(item)
                if "|" in tmp:
                    index = tmp.index("|")
                    item1 = tmp[:index]
                    item2 = tmp[index+1:]
                    if len(word) > i+1:
                        wordlist.append(newlist + item1 + word[i+1:])
                    else:
                        wordlist.append(newlist + item2)
                    newlist += item2
                else:
                    newlist += tmp
            wordlist[w] = copy.deepcopy(newlist)
            word = copy.deepcopy(newlist)
    print(wordlist)
    for i in wordlist:
        summa += messagelist.count("".join(i))
    print(summa)


Part111()
print("lol")

        for item in ruledict[key]:
            if item in ["a","b"]:
                return item
            else:
                return "("+"".join("|" if i == "|" else rec(i) for i in item)+")"