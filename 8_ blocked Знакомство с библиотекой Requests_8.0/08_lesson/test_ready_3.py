from Create import ProjectAPI

BASE_URL = 'https://ru.yougile.com'
TOKEN = 'UpSK5KaZjP9E0huMp1GGaQViSLzfz2siJxfw1fsUT5S+fDLcrbhgtPAohn4Or3IV'

api = ProjectAPI(BASE_URL, TOKEN)


def test_get_project_positive():
    create_response = api.create_project(
        'Тестовый проект для получения',
        {'11fc3ab1-233f-4c61-8c00-ff44380acf3a': 'worker'}
    )
    assert create_response.status_code == 201, f"Создание проекта не удалось: {create_response.text}"
    project_id = create_response.json().get('id')

    response = api.get_project(project_id)
    assert response.status_code == 200, f"Получение проекта завершилось ошибкой: {response.text}"
    data = response.json()
    assert data.get('id') == project_id
    assert data.get('title') == 'Тестовый проект для получения'

def test_update_project_positive():
    create_resp = api.create_project(
        'Проект для обновления',
        {'11fc3ab1-233f-4c61-8c00-ff44380acf3a': 'admin'}
    )
    assert create_resp.status_code == 201
    project_id = create_resp.json().get('id')
    response = api.update_project(
        project_id,
        'Обновлённый проект',
        {'11fc3ab1-233f-4c61-8c00-ff44380acf3a': 'admin'}
    )
    assert response.status_code == 200


def test_create_project_negative():
    response = api.create_project('', {})
    assert response.status_code != 201

def test_update_project_negative():
    response = api.update_project(
        'некорректный-id',
        'Обновлённый проект',
        {'11fc3ab1-233f-4c61-8c00-ff44380acf3a': 'admin'}
    )
    assert response.status_code != 200

def test_get_project_negative():
    response = api.get_project('невалидный-идентификатор')
    assert response.status_code != 200
