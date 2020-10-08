#2 Even Fibonacci numbers

ls = [1,2]
a = 1
b = 2
s = 0
t = 0
for i in range(1000):
    ls.append(a+b)
    a = b
    b = ls[-1]
    if ls[-1]>4000000:
        break
    else:
        t = i

for i in ls:
    if i%2==0:
        s=s+i

print(s)
