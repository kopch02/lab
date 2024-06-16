from requests import post, get, delete
import pytest

print(get('http://localhost:5000/api/v2/users').json())



print(get('http://localhost:5000/api/v2/users/4').json())

print(get('http://localhost:5000/api/v2/users/999').json())


print(post('http://localhost:5000/api/v2/users').json())
print(post('http://localhost:5000/api/v2/users',
           json={'name': 'Заголовок'}).json())

print(post('http://localhost:5000/api/v2/users',
           json={'surname': 'фамилия',
                 'name': 'имя',
                 'position': 'позиция',
                 'speciality':'специальность',
                 'age': 21}).json())



print(delete('http://localhost:5000/api/v2/users/999').json())

print(delete('http://localhost:5000/api/v2/users/4').json())