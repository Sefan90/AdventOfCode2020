                combi = []
                for fo in range(1,len(foundx)+1):
                    combi += [sum(x) for x in itertools.combinations(foundx, fo)]
                for c in range(1,len(combi)):
                    tmp = "{:00"+str(len(combi)//2)+"b}"
                    combival = [v for v in tmp.format(c)]
                    combivalue = copy.deepcopy(binvalue)
                    val = 0
                    for m in range(len(combivalue)):
                        if combivalue[m] == "X":
                            combivalue[m] = combival[val]
                            val += 1
                    mem[str(combi[c])] = "".join([str(b) for b in combivalue])




