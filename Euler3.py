startnumber = 122344 #600851475143 13195  26171
numberprimelist = []
primelist = []
listindex = 0




lower = 1
upper = 10000
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           primelist.append(num)

print(primelist)



while startnumber != 0 and listindex < len(primelist) :
    if startnumber % primelist[listindex] == 0:
        numberprimelist.append(primelist[listindex])
        startnumber = startnumber // primelist[listindex]
        print(startnumber)
    else:
        listindex += 1
        if listindex >= len(primelist):
            break

        




print("\n")
print(numberprimelist)



    
    






