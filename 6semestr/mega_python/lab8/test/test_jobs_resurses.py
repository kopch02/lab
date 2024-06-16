from requests import post, get, delete
import pytest

print(get('http://localhost:5000/api/v2/jobs').json())



print(get('http://localhost:5000/api/v2/jobs/4').json())

print(get('http://localhost:5000/api/v2/jobs/999').json())


print(post('http://localhost:5000/api/v2/jobs').json())
print(post('http://localhost:5000/api/v2/jobs',
           json={'job': 'Заголовок'}).json())

print(post('http://localhost:5000/api/v2/jobs',
           json={'team_leader': 'ответсвенный',
                 'job': 'Текст работы',
                 'work_size': 12,
                 'collaborators':'1;7;2',
                 'is_finished': False}).json())



print(delete('http://localhost:5000/api/v2/jobs/999').json())

print(delete('http://localhost:5000/api/v2/jobs/4').json())