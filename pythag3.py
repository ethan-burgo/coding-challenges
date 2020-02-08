import math
"""a = int(input("enter the first number: "))
b = int(input("enter the second number: "))

c = math.sqrt((a**2 + b**2))
print(c)"""

count = 1
while count < 1000:
    for x in range(1, 1000):
        a = count
        b = x
        cSq = math.sqrt((a**2 + b**2))
        if cSq.is_integer():
           if a + b + cSq == 1000:
               print(a*b*cSq)
    count = count + 1
