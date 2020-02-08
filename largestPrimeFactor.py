num = 13195//2
"""count = num
prime = False
while count <= num and prime == False:
    for x in range(7, count):
        if num % x == 0:
            prime = False
            count = count -1
            print(count)
            continue
        else:
            prime = True

    if prime == True:
        print(num)"""


count = num
prime = False
while count <= num and prime == False:
    for x in range(7, count):
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            count = count - 1
            continue
        if num % x == 0:
            prime = False
            count= count-1
            print(count)
            continue
        else:
            prime = True

    if prime == True:
        print(num)
