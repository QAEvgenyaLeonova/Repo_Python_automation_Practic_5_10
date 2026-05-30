import requests

base_url = 'https://ru.yougile.com'
token = 'Bearer knEfLTnRWJkr13OyzIFSKzJY6-FGRviWx+Mdsn7ftoM4HK0E+m+d6gv+fuk3+y47'


def test_authorization_yougile():
    creds = {
        "login": "testing.qa@inbox.ru",
        "password": "Asdf!2218"
    }
    response = requests.post(base_url + '/api-v2/auth/companies', json=creds)
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json; charset=utf-8'

def test_company_yougile_all_list():
    creds = {
        "login": "testing.qa@inbox.ru",
        "password": "Asdf!2218"
    }
    response = requests.post(base_url + '/api-v2/auth/companies', json=creds)
    response_body = response.json()
    assert response.status_code == 200

def test_project_yougile_all_list():
    headers = {
        "Authorization": f"{token}"
    }
    response = requests.get(base_url + '/api-v2/projects', headers=headers)
    assert response.status_code == 200, f"Ошибка: {response.status_code}"
    response_body = response.json()
    assert response.headers['content-type'] == 'application/json; charset=utf-8'

def test_all_list_staff_yougile():
    headers = {
        "Authorization": f"{token}"
    }
    response = requests.get(base_url + '/api-v2/users', headers=headers)
    response_body = response.json()
    assert response.status_code == 200
    print(response_body)

def test_create_project_yougile():
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    create = {
        "title": "Мой проект",
        "users": {
            "11fc3ab1-233f-4c61-8c00-ff44380acf3a": "admin"
        }
    }
    response = requests.post(base_url + '/api-v2/projects', json=create, headers=headers)
    response_body = response.json()

    # Проверка, что статус-код равен 201
    assert response.status_code == 201, f"Unexpected status code: {response.status_code}. Response: {response_body}"



