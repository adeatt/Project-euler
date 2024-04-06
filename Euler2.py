
list1 = [1,2]
list2 = [2]
listnum1 = 0
listnum2 = 1

while list1[-1] < 4000000:
    list1.append(list1[listnum1] + list1[listnum2])
    listnum1 += 1
    listnum2 += 1
    if list1[-1] %2 == 0:
        list2.append(list1[-1])

print(list1)
print("\n")
print(list2)

Answer = sum(list2)
print(Answer)


