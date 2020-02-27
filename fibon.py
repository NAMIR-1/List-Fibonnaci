def getFib(n):
    fibon = [0,1]
    Two = [0,1]
    counter = 3
    while counter <= n and n > 1:
        nextFib = Two[0] + Two[1]
        Two[0] = Two[1]
        Two[1] = nextFib
        counter += 1
        fibon.append(nextFib)    
    return print(fibon) 


getFib(9)
