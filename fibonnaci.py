
n = int(input("enter num: "))
def fibonnaci(n):
    list = [0,1]
    count = 2
    while count <= n+2:
        list.append(list[count-2] + list[count-1])
        count = count + 1

    return(list)

print(fibonnaci(n)[n-1])
