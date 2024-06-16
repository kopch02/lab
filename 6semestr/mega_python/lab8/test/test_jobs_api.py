from requests import post, get, delete, put
import pytest


def test_get_all():
    assert get('http://localhost:5000/api/jobs').json() == ""


print(get('http://localhost:5000/api/jobs').json())
print('\n')
print(get('http://localhost:5000/api/jobs/1').json())
print('\n')
print(post('http://localhost:5000/api/jobs', json={'job': 'megatest'}).json())
print('\n')
print(
    post('http://localhost:5000/api/jobs',
         json={
             'team_leader': 1,
             'job': 'megatest',
             'work_size': 11,
             'collaborators': '1;2;3;'
         }).json())

print(delete('http://localhost:5000/api/jobs/5'))
print('\n')
print(put('http://localhost:5000/api/jobs/4', json={'job': 'megatest'}))
print('\n')
print(
    put('http://localhost:5000/api/jobs/3',
        json={
            'team_leader': 1,
            'job': 'megatest',
            'work_size': 11,
            'collaborators': '1;2;3;'
        }).json())
