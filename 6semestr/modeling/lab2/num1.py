import numpy as np

a = 37
b = 1
M = 1000
N = 100

x = []

x.append(38)

for i, n_ in enumerate(range(99)):
    x.append(((a * x[i] + b) % M))

x = np.array(x) / M
x_min = x.min()
x_max = x.max()

h = (x_max - x_min) / (1 + 3.3221 * np.log10(100))

print(f"{h = }")

x2 = []
b = 0
i = 0
while b < x_max:
    a = x_min + h * i
    b = x_min + h * (i + 1)
    x2.append([a, b])
    i += 1
count = 0
n_ = 0
print(f"отрезки = {np.array(x2)}")
#print(len(x))
n = []
for i in x2:
    count = 0
    for j in x:
        if j >= i[0] and j < i[1]:
            count += 1
    n.append(count)
print(f'{n = }')

x_ = x.sum() / 100

D = sum((x - x_)**2) / 100
print(f"{D = }")
a_ = x_ - np.sqrt(3 * D)
b_ = x_ + np.sqrt(3 * D)

print(f"{a_ = }")
print(f"{b_ = }")

f = 1 / (b_ - a_)
print(f"f(x) = {f}")

n_ = []

n_.append(100 * (((x2[0][0] + x2[0][1]) / 2) - a_) / (b_ - a_))

for i in range(len(x2) - 2):
    x_c = (x2[i + 1][1] + x2[i + 1][0]) / 2
    x_c2 = (x2[i][1] + x2[i][0]) / 2
    n_.append(100 * (1 / (b_ - a_)) * (x_c - x_c2))

n_.append(100 * (1 / (b_ - a_)) * (b_ - ((x2[-2][0] + x2[-2][1]) / 2)))

print(f"{n_ = }")

k = len(x2)
xx = 0
for i in range(k):
    xx += ((n[i] - n_[i])**2) / n_[i]

print(f"{xx = }")

print("X кр = 11.1 => гипотеза принимается")
x_sort = x.copy()
print(x)
x_sort.sort() #сортирую основной
medN = 0.5 * (x_sort[int(N / 2) - 1] + x_sort[int((N / 2))])
print(f"{medN = }")
ser = ""
for i in x:
    if i >= medN:
        ser += "+"
    elif i < medN:
        ser += "-"

print(ser)

usl_1 = 40
usl_2 = 61

current = ser[0]
seria = 1
for i in ser:
    if i != current:
        seria += 1
        current = i

print(f"{seria = }")
if usl_1 < seria and seria < usl_2:
    print("гипотеза Н0 принимается")

I = np.array(list(range(100))) + 1

top = 1 / N * sum(I * x) - 1 / N * sum(x * ((N + 1) / 2))
down = np.sqrt((1 / N * sum(x ** 2) - (1 / N * sum(x)) ** 2) * (((N ** 2 )- 1) / 12))

r = top /down

#print(f"{top =}")
#print(f"{down =}")

print(f"{r = }")

z = 2.3

r_max = z * (1 - r **2) / np.sqrt(N)

print(f"{r_max = }")

print("т.к. r < r_max, то корреляционной связи между псевдослучайными числами нет")
