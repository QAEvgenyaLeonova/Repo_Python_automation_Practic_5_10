import requests

base_url = 'http://5.101.50.27:8000'

def get_company_list(params_to_add = None):
    response = requests.get(base_url + '/company/list', params_to_add)
    return response.json()



#Получить список компаний
def test_simple_req():
    response = requests.get(base_url + '/company/list')
    response_body = response.json()
    first_company = response_body[0]
    assert first_company['name'] == 'QA Студия \'ТестировщикЪ\''
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
#Авторизация
def test_authorization():
    creds = {
        'username': 'harrypotter',
        'password': 'expelliarmus'
    }
    response = requests.post(base_url + '/auth/login', json=creds)
    assert response.status_code == 200
    assert response.json()['user_token'] is not None

#Создание компании
def test_create_company():
    company = {
        'name': 'python',
        'description': 'requests'
    }
    response = requests.post(base_url + '/company/create', json=company)
    assert response.status_code == 201

#Автотест. Получение списка компаний
def test_get_companies():
    response = requests.get(base_url + '/company/list')
    body = response.json()

    assert response.status_code == 200
    assert len(body) > 0

#Автотест. Active True == Fulse
def test_get_active_companies():
    response = requests.get(base_url + '/company/list')
    full_list = response.json()

    response_2 = requests.get(base_url + '/company/list?active=true')
    active_list = response_2.json()

    assert len(full_list) > len(active_list)
'''Если параметров будет много, то их удобнее записывать таким способом.
my_params = {'active' : 'true'}
response = requests.get(base_url+'/company/list', params=my_params)
filtered_list = response.json()'''