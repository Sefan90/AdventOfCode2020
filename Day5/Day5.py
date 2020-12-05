def Part1():
    f = open("input.txt","r")
    lines = f.readlines()
    seatID = []
    for i in lines:
        row = [0,127]
        column = [0,7]
        for l in range(len(i)):
            if l < 7:
                if i[l] == "F":
                    row[1] = row[1]-int((row[1]-row[0])/2+0.5)
                elif i[l] == "B":
                    row[0] = row[0]+int((row[1]-row[0])/2+0.5)
            else:
                if i[l] == "L":
                    column[1] = column[1]-int((column[1]-column[0])/2+0.5)
                elif i[l] == "R":
                    column[0] = column[0]+int((column[1]-column[0])/2+0.5)
        seatID.append(row[0]*8+column[0])
    print(max(seatID))

def Part2():
    f = open("input.txt","r")
    lines = f.readlines()
    seatID = []
    seatList = []
    for i in range(128):
        for j in range(8):
            seatList.append(i*8+j)
    for i in lines:
        row = [0,127]
        column = [0,7]
        for l in range(len(i)):
            if l < 7:
                if i[l] == "F":
                    row[1] = row[1]-int((row[1]-row[0])/2+0.5)
                elif i[l] == "B":
                    row[0] = row[0]+int((row[1]-row[0])/2+0.5)
            else:
                if i[l] == "L":
                    column[1] = column[1]-int((column[1]-column[0])/2+0.5)
                elif i[l] == "R":
                    column[0] = column[0]+int((column[1]-column[0])/2+0.5)
        seatID.append(row[0]*8+column[0])
    for i in seatID:
        seatList.remove(i)
    #Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
    seatList = [i for i in seatList if i-1 not in seatList and i+1 not in seatList] 
    print(seatList)

import time
start_time = time.time()
Part2()
print("--- %s seconds ---" % (time.time() - start_time))