num = 130
half = num//2
list = []
prime = False
count = 0
counter = 2

while prime == False:
    if half-count % counter == 0:
        count = count + 1
        continue

    if counter == half-count:
        if num % half-count == 0:
            list.append(half-count)
            prime = True
            continue
    else:
        counter = counter + 1
        continue

else:
    print(list)



print(13195/6597)
