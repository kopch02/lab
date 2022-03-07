def n1():
    from collections import Counter
    text="very very very big text"
    a=text.split()
    c=Counter(a)
    print(c)

def n2():
    try:
        n=int(input("сколько синонимов? ->"))
        ar={}
        ar2={}
        for x in range(n):
            first=input("1е слово->")
            second=input("2е слово->")
            ar[first]=second
            ar2[second]=first

        f=input("для кого найти синоним?->")
        print(ar[f])
    except:
        print(ar2[f])

def n3():
    n=int(input("сколько записей?->"))
    ar={}
    for x in range(n):
        f=input("Фмилия кандидидата ->").lower()
        g=int(input("сколько голосов->"))
        if f in ar:  
            ar[f]=ar[f]+g
        else:
            ar[f]=g
    l=list(ar.keys())
    l.sort()
    for i in l:
        print(i, "-", ar[i])

def n4():
    n=int(input("количество файлов->"))
    ar={}
    ar2={}
    q={}
    for x in range(n):
        f=input("имя файла->")
        ar[f]=input("разрешённые опирации->")
    m=int(input("сколько запросов?->"))
    for i in range(m):
        f=input("файл->")
        o=input("опирации->")
        ar2[f]=o
        if o in ar[f]:
            print(ar[f])
            print("OK")
        else:
            print(ar[f])
            print("Access denied")
        
def n5():
    n=int(input("количесов строк->"))
    a=[]
    for x in range(n):
        a.append(input())
