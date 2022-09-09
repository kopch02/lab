import numpy as np

# num1
arr_1 = np.zeros((3, 4)) + 3
# num2
arr_2 = np.random.randint(0, 9, size=(2, 4))
# num3
print("arr1 size: ", arr_1.size, "\narr2 size: ", arr_2.size)
# num4
c = np.concatenate((arr_1, arr_2), axis=0)
print(c)
# num5
arr_3 = np.array((1, 8, 6, 5, 8, 3))
print(arr_3)
# num6
arr_4 = (arr_3 * 3) + 1
print(arr_4)
# num7
arr_5 = arr_3.reshape(2, 3)
print(arr_5)
# num8
print(np.amin(arr_5, axis=1))
# num9
print(np.mean(arr_5))
# num10
arr_6 = np.linspace(0, 10, 11)**2
print(arr_6)
# num11
print(arr_6[1::2])
# num12
print(arr_6[::-1])
# num13
arr_6[1::2] = 2
print(arr_6)
# num14
print(49 in arr_6)
# num15
a = np.random.randint(0,20,size=(3,4)) - 10
b = a[a < 0]
print(a)
print(b)