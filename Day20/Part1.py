import collections
file = open("input.txt","r").readlines()
tiledict = {}
matchdict = collections.defaultdict(set)
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
                    if v == iv or v == iv[len(iv)::-1]:
                        matchdict[key].add(ikey)
                        matchdict[ikey].add(key)
                        matchfound = True
                        break
print(tiledict)
print(matchdict)

for k,v in matchdict.items():
    if len(v) == 2:
        summa *= int(k)

print(summa)