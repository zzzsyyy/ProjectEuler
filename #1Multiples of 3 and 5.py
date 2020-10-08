#1:Multiples of 3 and 5

s = 0
for i in range(1000):
    if i%15==0:
        s=s+i
    else:
        if i%3==0:
            s=s+i
        else:
            if i%5==0:
                 s=s+i

print(s)
