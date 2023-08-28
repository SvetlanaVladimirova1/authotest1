import requests
import yaml

with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)
address = data['address2']

S = requests.Session()


def test_rest(user_login):
    res = (S.get(url=address, headers={'X-Auth-Token': user_login}).json()['data'])
    r = [i['title'] for i in res]
    assert r, 'Test FAILED'
    print(r)


def test_rest1(user_login, user_posts):
    res = (S.get(url=address, headers={'X-Auth-Token': user_login}).json()['data'])
    r = [i['description'] for i in res]
    assert r, 'Test FAILED'
    print(r)


