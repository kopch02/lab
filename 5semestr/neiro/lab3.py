import pandas as pd

num1 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print(num1)

print(num1['d'])

print(num1[1])

num1['f'] = 6
print(num1)

print(num1[2:5])

df = pd.DataFrame(data=[[1, 2], [5, 3], [3.7, 4.8]], columns=['col1', 'col2'])
print(df)


print(df["col1"][2])


df["col2"][1]=9
print(df)


print(df[1:3])

df['col3']=df['col1']*df['col2']
print(df)