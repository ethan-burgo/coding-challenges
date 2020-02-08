num = 13
pCount = 6
count = 14
prime = False
pList = [count]
amount = [pCount]

while pCount < 10001:
    for x in range(2, count//2):
        if count % x == 0:
            prime = False
            count = count + 1
            break

        else:
            prime = True

    if prime == True:
        pCount = pCount + 1
        count = count +1
        if pCount == 10001:
            pList.append(count-1)

print(pList)
