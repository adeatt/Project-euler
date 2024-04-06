num1 = 100
num2 = 100
listanswer = []
polindrom = []

while num2 <= 999:
    if num1 <= 999:
        answer = num1 * num2
        answer = str(answer)
        if answer[0] == answer[-1] and answer[1] == answer[-2] and answer[2] == answer[-3]:
            answer = int(answer)
            polindrom.append(answer)
        num1 += 1
    else:
        num2 += 1
        num1 = 100
    
        
polindrom.sort()
print(polindrom[-1])












