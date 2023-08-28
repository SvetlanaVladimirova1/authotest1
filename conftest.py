import pytest
import requests
import yaml

with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)
username, password, address, address2, title, description, content = data['username'], data['password'], data['address'], data['address2'], data['title'], data['description'], data['content']

S = requests.Session()


@pytest.fixture()
def user_login():
    res1 = S.post(url=address, data={'username': username, 'password': password})
    return res1.json()['token']


@pytest.fixture()
def user_posts():
    res1 = S.post(url=address2, headers={'X-Auth-Token': '47d89fb7c09b48465dac63fbb3976adb'}, data={'title': title, 'description': description, 'content': content})
    return res1.json()

