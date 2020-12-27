import collections

class Tile:
    def __init__(self, imagetile):
        self.image = imagetile
        self.update()

    def update(self):
        self.right = "".join([i[-1:]for i in self.image])
        self.left = "".join([i[:1]for i in self.image])
        self.bottom = self.image[-1]
        self.top = self.image[0]

    def items(self):
        return self.top, self.right, self.bottom, self.left
    
    def rotate(self):
        self.image = [''.join(reversed(row)) for row in zip(*self.image)]
        self.update()
    
    def flip(self):
        tmp = []
        for row in self.image:
            tmp.append(reversed(row))
        self.image = tmp
        self.update()

file = open("testinput.txt","r").readlines()
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
        tiledict[currentkey] = Tile(imagetile)
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
imagerow = 0
tilelist = []
while currentTile not in tilelist:
    tilelist.append(currentTile)
    lastitem = currentTile
    goright = True
    godown = False
    while currentTile == lastitem:
        for item in matchdict[currentTile]:
            if item[1] not in tilelist:
                print(item)
                if item[0] == "R": 
                    currentTile = item[1]
                    tmprow = imagerow
                    for t in tiledict[currentTile]["I"]:
                         [tmprow] += " " + t
                        tmprow += 1
                elif item[0] == "T":
                    godown = False
                    currentTile = item[1]
                    tmprow = imagerow
                    for t in tiledict[currentTile]["I"]:
                        image[tmprow] += " " + t
                        tmprow += 1
                elif item[0] == "B":
                    godown = False
                    currentTile = item[1]
                    tmprow = imagerow
                    for t in tiledict[currentTile]["I"]:
                        image[tmprow] += " " + t
                        tmprow += 1
                elif item[0] == "L":
                    godown = False
                    currentTile = item[1]
                    tmprow = imagerow
                    for t in tiledict[currentTile]["I"]:
                        image[tmprow] += " " + t
                        tmprow += 1
            else:
                break

for i in image:
    print(i)