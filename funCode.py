unsorted = [19,0,15,12,9,7,1,14,10,4,6,8,11,3,18,5,17,20,13,2,16]
#unsorted = [2,5,4,1,3]
sorted = []

count = 0
counter = 0
unsortedLen = len(unsorted)
sortedLen = len(sorted)


while count < unsortedLen-1:
    if unsorted[count] > unsorted[count + 1]:
        temp = unsorted[count]
        unsorted[count] = unsorted[count +1]
        unsorted[count+1] = temp

        count = 0

    else:
        counter = counter + 1
        count = count + 1

print(unsorted)
