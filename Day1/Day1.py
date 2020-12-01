def Part1():
    lines = open("input.txt","r").readlines() 
    for i in lines:
        for j in lines:
            if int(i)+int(j) == 2020:
                print(int(i)*int(j))
                quit()
def Part2():
    lines = open("input.txt","r").readlines()
    for i in lines:
        for j in lines:
            if int(i)+int(j) < 2020:
                for k in lines:
                    if int(i)+int(j)+int(k) == 2020:
                        print(int(i)*int(j)*int(k))
                        quit()
Part2()