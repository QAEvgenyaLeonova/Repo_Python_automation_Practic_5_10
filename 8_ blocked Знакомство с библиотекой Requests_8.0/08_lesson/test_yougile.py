import pytest
from Create import ProjectAPI

# Данные для теста (можно вынести в отдельный конфиг)
BASE_URL = 'https://ru.yougile.com'
TOKEN = 'cgetG8Gzq-JT0vnyqb4sXvsVldUdlPxSo3XWSJeDOygQNnux0lsRzMrpxOAxoETQ'  # Ваш токен

# Создаем экземпляр класса для тестов
api = ProjectAPI(BASE_URL, TOKEN)


def test_create_project():
    """Тест на успешное создание проекта (статус 201)."""

    # Данные для запроса (из вашего примера)
    title = "ГосУслуги"
    users = {
        "4902b994-b806-4af4-acec-018ea5ea6468": "worker",
        "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018": "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
    }

    # Вызываем метод из класса
    response = api.create_project(title, users)

    # Проверки (ассерты)
    assert response.status_code == 201, "Статус ответа не 201 Created"
    assert "id" in response.json(), "В ответе отсутствует поле 'id'"
    assert response.json()["id"], "ID проекта пустое"


def test_create_project_invalid_title():
    """Тест на обработку ошибки (невалидный заголовок)."""
    response = api.create_project("", {"test": "worker"})  # Пустой заголовок
    assert response.status_code >= 400, "Ожидалась ошибка валидации"
