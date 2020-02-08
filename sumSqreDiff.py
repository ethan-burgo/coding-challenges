list1 = []
list2 = []
for x in range(1, 101):
    x = x **2
    list1.append(x)

for y in range(1, 101):
    list2.append(y)

square = (sum(list2))**2

print(square-sum(list1))
