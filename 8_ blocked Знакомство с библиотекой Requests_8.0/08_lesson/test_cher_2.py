import pytest
import requests

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
    response = requests.post(f'{base_url}/api-v2/projects', json=create, headers=headers)
    assert response.status_code == 201, f'Ошибка создания: {response.status_code}'
    response_body = response.json()
    project_id = response_body.get('id')
    assert project_id is not None, 'ID проекта не получен'
    return project_id

def test_create_project_yougile(create_project):
    project_id = create_project
    print(f'ID созданного проекта: {project_id}')

def test_update_project_yougile(create_project):
    project_id = create_project
    update_data = {
        'title': 'Обновленный проект',
        'users': {
            '11fc3ab1-233f-4c61-8c00-ff44380acf3a': 'admin'
        }
    }
    response = requests.put(f'{base_url}/api-v2/projects/{project_id}', json=update_data, headers=headers)
    assert response.status_code == 200, f'Ошибка обновления: {response.status_code}'
    print(f'Проект {project_id} успешно обновлен')

def get_project_by_id(project_id):
    response = requests.get(f'{base_url}/api-v2/projects/{project_id}', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Ошибка получения проекта: {response.status_code}')
        return None

def test_get_project():
    project_id = '4f6f0391-0f94-4d30-9b0e-99430a36d4fb'
    project_info = get_project_by_id(project_id)
    if project_info:
        print(project_info)
    else:
        print('Не удалось получить информацию о проекте')

def delete_project_yougile(project_id):
    response = requests.delete(f'{base_url}/api-v2/projects/{project_id}', headers=headers)
    assert response.status_code == 200, f'Ошибка удаления: {response.status_code}'
    print(f'Проект {project_id} успешно удален')