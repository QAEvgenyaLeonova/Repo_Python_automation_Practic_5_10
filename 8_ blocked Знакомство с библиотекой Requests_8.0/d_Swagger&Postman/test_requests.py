import requests

base_url = 'http://5.101.50.27:8000'

def test_simple_red():
    resp_get = requests.get(base_url + '/company/list')

    response_body = resp_get.json()
    first_company = response_body[0]
    assert first_company['name'] == "QA Студия 'ТестировщикЪ'"
    assert resp_get.status_code == 200
    assert resp_get.headers['Content-Type'] == 'application/json'

def test_auth():
    creds = {
        'username': 'harrypotter',
        'password': 'expelliarmus'
    }
    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()['user_token']
    assert resp.status_code == 200
    assert token

def test_create_company():
    creds = {
        'username': 'harrypotter',
        'password': 'expelliarmus'
    }
    company = {
        'name': 'python',
        'description': 'request',
        'is_active': True
    }
    #Авторизация
    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()['user_token']

    #Создание
    my_headers = {}
    my_headers['x-client-token'] = token
    resp = requests.post(base_url + '/company/create', json=company, headers = my_headers)
    assert resp.status_code == 201

