a = [123,"qwe",True,"1234",2.5]
print(a)
a.append(45)
print(a)
del a[2]
print(a)

p = print

b = [1,23,4, p]
print(b[0] + b[1])
b[-1]("qweqwe")
b.insert(0,123)
print(b)

#кортёж
a = (123,123,123)
#множество
a = {1,2,4,5,5,5,5}
a.add(123)
a.remove(1)
print(a)
#словарь
# элементы через запятую
# каждый элемент это - ключ:значение
a = {"one":1,
     "two":2,
     "3":"three"}

a["new"] = 123
a["one"] = 123
print(a["new"])

a = [1,
     [123,2,
      {"one":[123,123],
       "two":{1,2,3}}]]
print(a[1][2]["one"][1])
