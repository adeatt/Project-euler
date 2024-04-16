primelist = [2,]



for num in range(3, 2000001, 2):

    for n in range(0, len(primelist)-1):
        if num % primelist[n] == 0:
            break
    else:
        primelist.append(num)       


print(sum(primelist))             #could take up to 5 minutes or more idk. at least its faster than euler7
