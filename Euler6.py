
squarenumlist = []

for n in range(1, 101):
    i = pow(n, 2)
    squarenumlist.append(i)

sumofsquares = sum(squarenumlist)
print(sumofsquares)


x = 0
for n in range(1, 101):
    x += n
squareofsum = pow(x, 2)
print(squareofsum)


answer = squareofsum - sumofsquares
print(answer)



