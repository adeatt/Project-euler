answerlist=[]
a = 1
b = 1
c = 1
alist = []
blist = []
clist = []
import math

while b < 400 :
    c = math.sqrt((a*a) + (b*b))

    if a<b<c and c%1 == 0:
        alist.append(a)
        blist.append(b)
        clist.append(c)
    
    print(a,b,c)
    a += 1
    if a >= 400:
        b += 1
        a = 2

print("\n")
print("abc lists were successuful, beginning sorting")
print("\n")

for n in range(0, len(alist)):
    answer = alist[n] + blist[n] + clist[n]
    if answer == 1000:
        product = alist[n]*blist[n]*clist[n]
        print(product)