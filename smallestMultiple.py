divisible = False
count = 2520
bruh = 11

while divisible == False or bruh <= 20:
    if count % 19 == 0 and count % 17 == 0 and count % 13 == 0 and count % 7 == 0:
        for x in range(1, bruh):
            if count % x == 0:
                divisible = True
            else:
                divisible = False
                count = count + 1
                break
    else:
        count = count+1

    if divisible == True:
        bruh = bruh + 1

print(count, bruh)

#12252240
