test = ['#.#.#####.', '.#..######', '..#.......']
print("".join([i[-1:] for i in test]))

            for allergen in values:
                if allergen in fooddict[key][0]:
                    continue
                else:
                    fooddict[key][0].add(allergen)
                    fooddict[key][1].add(allergen)

import collections
file = open("testinput.txt","r").readlines()
fooddict = {}
for line in file:
    k, v = [i.replace(")\n","") for i in line.split(" (contains ")]
    values = [i for i in k.split()]
    keys = [i for i in v.split(", ")]
    for key in keys:
        if key in fooddict.keys():
            if key == "sbzzf":
                print("hej")
            tmp = list(fooddict[key][0]-set(values))
            for t in tmp:
                fooddict[key][1].add(t)
            for val in values:
                fooddict[key][0].add(val)
        else:
            fooddict[key] = [set(values),set()]
print(fooddict)
