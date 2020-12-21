import collections
file = open("input.txt","r").readlines()
tiledict = {}
matchdict = collections.defaultdict(list)
currentkey = ""
imagetile = []
summa = 1
for row in file:
    if "Tile" in row:
        currentkey = row[5:].replace(":","").replace("\n","")
        imagetile = []
    elif row == "\n":
        tmpdict = {}
        tmpdict["T"] = imagetile[0]
        tmpdict["B"] = imagetile[-1]
        tmpdict["R"] = "".join([i[-1:]for i in imagetile])
        tmpdict["L"] = "".join([i[:1]for i in imagetile])
        tmpdict["I"] = imagetile   
        tiledict[currentkey] = tmpdict
    else:
        imagetile += [row.replace("\n","")]
for key, value in tiledict.items():
    for k, v in value.items():
        matchfound = False
        for ikey, ivalue in tiledict.items():
            if matchfound == True:
                break
            elif key != ikey:
                for ik, iv in ivalue.items():
                    if v == iv:
                        matchdict[key].append([k,ikey,ik,False])
                        matchfound = True
                        break
                    elif v == iv[len(iv)::-1]:
                        matchdict[key].append([k,ikey,ik,True])
                        #matchdict[ikey].append([ik,key,k])
                        matchfound = True
                        break
#print(tiledict)
print(matchdict)

currentTile = ""
for k,v in matchdict.items():
    if len(v) == 2:
        summa *= int(k)
        if currentTile == "" and ((v[0][0] == "B" and v[1][0] == "R" and v[0][3] == False) or (v[0][0] == "R" and v[1][0] == "B" and v[0][3] == False)):
            currentTile = k
print(summa)

print(matchdict[currentTile])

image = tiledict[currentTile]["I"]
tilelist = []
while currentTile not in tilelist:
    tilelist.append(currentTile)
    lastitem = []
    for item in matchdict[currentTile]:
        if item[0] == "R":
            lastitem = item



print(image)