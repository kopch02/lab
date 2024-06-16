res = "1 1 0 1 0 1 0 1 0"

#делим на 2 интервала от 0 до 0.5 и от 0.5 до 1
#т.к. у нас первым первым число 1 , то берём правый

ab = [0, 1]
res = res.split()
print(res)

for i in res:
    a = (ab[1] - ab[0]) / 2
    if int(i) == 1:
        ab[0] = ab[0] + a
    else:
        ab[1] = ab[1] - a
    print(ab, i)


x=0.2152
for i in range(100):    
    print(x, str(x**2)[:10])
    x = int(str(x**2)[4:8]) / 10000