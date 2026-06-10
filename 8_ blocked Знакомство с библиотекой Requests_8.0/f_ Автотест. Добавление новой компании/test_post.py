import requests

base_url = 'http://5.101.50.27:8000'

def get_company_list(params_to_add = None):
    resp = requests.get(base_url + '/company/list', params=params_to_add)
    return resp.json()



def get_token(user = 'harrypotter', password = 'expelliarmus'):
    creds = {
        'username': user,
        'password': password
    }
    resp = requests.post(base_url + '/auth/login', json=creds)
    return resp.json()['user_token']



def create_company(name, description=''):
    company = {
        'name': name,
        'description': description,
        'is_active': True
    }
    my_headers = {}
    my_headers['x-client-token'] = get_token()
    resp = requests.post(base_url + '/company/create', json=company, headers=my_headers)
    return resp.json()



def test_get_companies():
    body = get_company_list()
    assert len(body) > 0 #== X

def test_get_active_companies():
    #Получить список всех компаний
    full_list = get_company_list()

    #Получить список активных компаний
    filtered_list = get_company_list(params_to_add= {'active': True})

    #Проверить что список 1 > больше списка 2
    assert len(full_list) > len(filtered_list)



def test_add_new():                              # Получить количество компаний до создания
    body = get_company_list()
    len_before = len(body)
    name = 'Autotest'                            # Создать новую компанию
    description = 'Decsr'
    result = create_company(name, description)
    new_id = result['is_active']
    body = get_company_list()                    # Получить, количество опять после создания
    len_after = len(body)
    assert  len_after - len_before == 1          # Проверить, что стало + 1
    # Проверить название и описание последней компании
    # Проверить, что Active последней компании в списке равен ответу из шага 2
    assert body[-1]['name'] == name
    assert body[-1]['description'] == description
    assert body[-1]['is_active'] == True




