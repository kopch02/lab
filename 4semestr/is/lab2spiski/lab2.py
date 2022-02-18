def n1():
    stroka = input()
    n = len(stroka)
    if n <= 2:
        print("слишком маленькая строка!!!!")
        quit()
    print(stroka[2])
    print(stroka[-2])
    print(stroka[:5])
    print(stroka[:n - 2])
    print(stroka[:n:2])
    print(stroka[1:n:2])
    print(stroka[::-1])
    revers = stroka[::-1]
    print(revers[:n:2])
    print(n)


def n2():
    stroka = input()
    n = len(stroka)
    two = n // 2
    one = n - two
    stone = stroka[:n - two]
    sttwo = stroka[one:n]
    string = str(sttwo) + str(stone)
    print(string)


def n3():
    stroka = input()
    n = len(stroka)
    a = ""
    b = False
    for x in range(1, n):
        if stroka[x] == "h":
            x += 1
            while True:
                a += stroka[x]
                x += 1
                if stroka[x] == "h":
                    b = True
                    break
            if b == True:
                break
    print(a[::-1])


def n4():
    stroka = input()
    n = len(stroka)
    l = list(stroka)
    if "f" in l:
        s = (l.count("f"))
        if s == 1:
            a = l.index("f")
            print(a + 1)
            quit()
        else:
            a = l.index("f")
            print(a + 1)
            revers = stroka[::-1]
            r = list(revers)
            b = r.index("f")
            b -= n
            b *= -1
            print(b)
    else:
        quit()


def n5():
    a = [1, 2, 2, 3, 3, 3, 5, 77, 6, 3, 5]
    n = len(a)
    for x in range(1, n):
        if a[x] > a[x - 1]:
            print(a[x])


def n6():
    a = [-1, 2, -2, -3, 3, -3, 5, -77, -6, 3, 5]
    n = len(a)
    for x in range(1, n):
        if a[x] < 0 and a[x - 1] < 0:
            print(a[x - 1], a[x], sep=" ")
            quit()
        if a[x] > 0 and a[x - 1] > 0:
            print(a[x - 1], a[x], sep=" ")
            quit()


def n7():
    a = [-1, 2, -2, -3, 3, -3, 5, -77, -6, 3, 5]
    n = []
    for number in a:
        if number in n:
            continue
        else:
            n.append(number)
    print(n)


def n8():
    def inp(a):
        for x in range(8):
            a.append("^")
    f0=[]
    f1=[]
    f2=[]
    f3=[]
    f4=[]
    f5=[]
    f6=[]
    f7=[]
    f8=[]
    f=[f0,f1,f2,f3,f4,f5,f6,f7]
    fc=[]
    
    for i in f:
        inp(i)
    
    for i in range(8):
        a=int(input("1я координата ферзя №%s:"%(i+1)))
        b=int(input("2я координата ферзя №%s:"%(i+1)))
        print("\n")
        if a>8 or b>8 or a<=0 or b<=0:
            print("координаты должны быть в пределах от 1 до 8 (включительно)")
            quit()
        else:
            c=str(a)+str(b)
            if c in fc:
                print("такие координаты уже есть!!")
                quit()
            fc.append(c)
            f[a-1][b-1]="f"
    #вывод доски
    for i in range(9):
        print(i,end="   ")
    print()
    for i in range(9):
        print("____",end="")
    print()
    for i in range(8):
        print(i+1,"| ",end="")
        for x in range(8):
            print(f[i][x],end="   ",)
        print()
    #проверка
    p=8
    for i in range(8):  
        for x in range(8): #проверка по горизонтали
            rev=f[i][::-1]
            q=f[i].index("f")
            w=rev.index("f")
            w-=7
            w*=-1
            if q!=w:   
                print("YES,1")
                quit()
        p-=1
        temp=0
        for x in range(8):
            if f[x][i]=="f":
                temp+=1
                if temp==2:
                    print("YES,2")
                    quit()
    f8=[0,0,0,0,0,0,0,0]
    f.append(f8)
    f[0].append(0)
    for i in range(8):
        f[i+1].append(0)
        for x in range(8):
            if f[i][x]=="f":
                if f[i][x]==f[i+1][x+1]:
                    print("YES,3")
                    quit()
    print("NO")
n8()