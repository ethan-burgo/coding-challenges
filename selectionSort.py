list = [5,8,2,4,0,1,7,6,10,9,3]

listLen = len(list)
count = 0
counter = 0

while count < listLen-1:
    if list[0] <= list[counter]:
        list[0] = list[counter]
        for x in range(0, counter):
            list[x] = list[x+1]

        count = 0

    counter = counter +1
