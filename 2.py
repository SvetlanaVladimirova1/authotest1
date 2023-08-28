import requests
import yaml

with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)
    username, password, address, address2, title, description, content = data['username'], data['password'], data['address'], data['address2'], data['title'], data['description'], data['content']

S = requests.Session()


def user_login():
    res1 = S.post(url=address, data={'username': username, 'password': password})
    return res1.json()


print(user_login()['token'])


def user_posts():
    res1 = S.post(url=address2, data={'title': title, 'description': description, 'content': content})
    return res1.json()


print(user_posts())