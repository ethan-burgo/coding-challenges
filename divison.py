num1 = 25
divisor = 2
count = 1
final = []
bruh = False
new = 25
if 0<=new<=1:
     bruh = True

while bruh==False:
    new = num1 - (divisor*count)
    #print(new)
    print(count)
    count = count + 1
    if 0<=new<=1:
         bruh = True
