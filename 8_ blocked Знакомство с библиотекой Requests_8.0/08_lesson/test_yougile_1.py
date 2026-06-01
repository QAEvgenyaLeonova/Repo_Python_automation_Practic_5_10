import requests
import pytest

base_url = 'https://ru.yougile.com'
token = 'Bearer UpSK5KaZjP9E0huMp1GGaQViSLzfz2siJxfw1fsUT5S+fDLcrbhgtPAohn4Or3IV'
headers = {
    'Authorization': token,
    'Content-Type': 'application/json'
}

@pytest.fixture
def create_project():
    create = {
        'title': 'Мой проект',
        'users': {
            '11fc3ab1-233f-4c61-8c00-ff44380acf3a': 'admin'
        }
    }
    response = requests.post(base_url + '/api-v2/projects', json=create, headers=headers)
    assert response.status_code == 201
    response_body = response.json()
    project_id = response_body.get('id')
    assert project_id is not None
    return project_id


def test_authorization_yougile():
    creds = {
        "login": "testing.qa@inbox.ru",
        "password": "Asdf!2218"
    }
    response = requests.post(base_url + '/api-v2/auth/companies', json=creds)
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json; charset=utf-8'
    print(response.json())

def test_company_yougile_all_list():
    creds = {
        "login": "testing.qa@inbox.ru",
        "password": "Asdf!2218"
    }
    response = requests.post(base_url + '/api-v2/auth/companies', json=creds)
    response_body = response.json()
    assert response.status_code == 200
    print(response)

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

def test_create_project_yougile(create_project):
    create = {
        "title": "Мой проект",
        "users": {
            "11fc3ab1-233f-4c61-8c00-ff44380acf3a": "admin"
        }
    }
    response = requests.post(base_url + '/api-v2/projects', json=create, headers=headers)
    response_body = response.json()

    assert response.status_code == 201, f'Unexpected status code: {response.status_code}. Response: {response_body}'

    project_id = response_body.get('id')
    if project_id:
        print(f"ID созданного проекта: {project_id}")
    else:
        print("ID проекта не найден в ответе.")

def test_update_project_yougile():
    create = {
        "title": "Мой новый проект_2",
        "users": {
            "11fc3ab1-233f-4c61-8c00-ff44380acf3a": "admin"
        }
    }