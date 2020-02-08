
terms = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

count = 55
counter = 11
listFactors = []
factors = len(listFactors)

while factors <= 200:
    for x in range(1, count+1):
        if (count+1) % x == 0:
            listFactors.append(x)

    print(listFactors)
    counter = counter+1
    count = count + counter
    factors = len(listFactors)
    print(factors)

    if factors == 8:
        print(count)
    else:
        listFactors *= 0
