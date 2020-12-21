import collections
file = open("input.txt","r").readlines()
fooddict = {}
foodlist = []
for line in file:
    k, v = [i.replace(")\n","") for i in line.split(" (contains ")]
    values = [i for i in k.split()]
    keys = [i for i in v.split(", ")]
    foodlist += values
    for key in keys:
        if key in fooddict.keys():
            tmp = set(values).intersection(fooddict[key][0])
            tmp2 = set(values).union(fooddict[key][1])
            fooddict[key] = [tmp,tmp2]
        else:
            fooddict[key] = [set(values),set(values)]

for i in fooddict.items():
    print(i)
withall = set()
noall = set()
counter = 0

for k, v in fooddict.items():
    for i in v[0]:
        withall.add(i)
    for i in v[1]:
        noall.add(i)

for i in noall:
    if i not in withall:
        counter += foodlist.count(i)

 

newdict = collections.OrderedDict(sorted(fooddict.items()))
output = ""
for k, v in newdict.items():
    output += str(list(v[0])[0])+","

print(output[:-1])