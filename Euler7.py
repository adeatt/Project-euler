primelist = []

for num in range(1, 200000):
    if num>1:
        for i in range(2, num):
            if num %i == 0:
                break
        else:
            primelist.append(num)
           

print(primelist)
print(len(primelist))
print(primelist[10000])
