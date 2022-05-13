import requests
#from geocode_key import api_key

response = requests.get(f"https://static-maps.yandex.ru/1.x/?ll=37.620070,55.753630&size=450,450&z=13&l=map&pt=37.620070,55.753630,pmwtm1~37.64,55.76363,pmwtm99")
'''https://static-maps.yandex.ru/1.x/?
ll=37.620070,55.753630    #Долгота и широта центра карты в градусах
size=450,450              #Ширина и высота запрашиваемого изображения карты (в пикселах)
z=13                      #Уровень масштабирования карты (0-17)
l=map                     #Перечень слоев, определяющих тип карты: map (схема), sat (спутник) и sat,skl (гибрид).
pt=37.620070,55.753630,pmwtm1~37.64,55.76363,pmwtm99  #метки на карте
spn=0.002,0.002'''         #область показа в градусах
print(response, type(response))


kemgu=requests.get(f"https://static-maps.yandex.ru/1.x/?ll=86.092277,55.351770&size=550,450&l=map&spn=0.002,0.002")
rayon=requests.get(f"https://static-maps.yandex.ru/1.x/?ll=86.079483,55.338328&size=550,450&l=map&spn=0.01,0.01")
Eiffel_Tower=requests.get(f"https://static-maps.yandex.ru/1.x/?ll=2.294494,48.858247&size=550,450&l=sat&spn=0.003,0.003")
vulkan=requests.get(f"https://static-maps.yandex.ru/1.x/?ll=158.833325,53.255274&size=550,450&l=sat&spn=0.02,0.02")
baikal=requests.get(f"https://static-maps.yandex.ru/1.x/?ll=107.6730584,53.405332&size=550,450&l=sat&spn=3,3")
baikonur=requests.get(f"https://static-maps.yandex.ru/1.x/?ll=63.286187,45.926092&size=550,450&l=sat&spn=0.03,0.03")




