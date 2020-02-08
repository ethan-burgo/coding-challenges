for x in range(1,100):
    if x % 3 == 0 and x % 5 == 0:
        print(str(x)+"fizbuzz")

    if x % 3 == 0 and x % 5 !=0:
        print(str(x)+"fiz")

    if x % 5 == 0 and x % 3 !=0:
        print(str(x)+"buzz")
