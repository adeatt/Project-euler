max = 1000
num = 1
list1 = []
while num < max:
    if num % 3 == 0  or num % 5 == 0 :
        list1.append(num)
        num += 1
    else:
        num += 1


print(list1)
Answer = sum(list1)
print(Answer)



