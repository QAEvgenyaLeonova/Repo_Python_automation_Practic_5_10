from CompanyApi_3 import CompanyApi
from CompanyTable_3 import CompanyTable

api = CompanyApi("http://5.101.50.27:8000")
db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")

def test_get_companies():
    # 1. Получить список через API
    api_result = api.get_company_list()

    # 2. Получить список через БД
    db_result = db.get_companies()

    # 3. Проверить, что длины списков равны
    assert len(api_result) == len(db_result), f"Длина списков не совпадает: API={len(api_result)}, DB={len(db_result)}"

# Проверка получения активных компаний
def test_get_active_companies():
    full_list = api.get_company_list()
    filtered_list = api.get_company_list(params_to_add={"active": "true"})
    assert len(full_list)  > len(filtered_list)

 # Проверка добавления новой компании
def test_add_new():
    body = api.get_company_list()
    len_before = len(body)
    name = "Autotest"
    descr = "Descr"
    api.create_company(name, descr)

    body = api.get_company_list()
    len_after = len(body)

    assert len_after - len_before == 1
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr

def test_get_one_company():
    # Создаем компанию
    name = "VS Code"
    descr = "IDE"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # Обращаемся к компании
    new_company = api.get_company(new_id)

    # Проверим название, описание и статус новой компании:
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["is_active"] is True

def test_edit():
    name = "Company to be edited"
    descr = "Edit me"
    result = api.create_company(name, descr)
    new_id = result["id"]

    new_name = "Updated"
    new_descr = "_upd_"

    edited = api.edit_company(new_id, new_name, new_descr)

    # Проверяем, что название компании поменялось
    assert edited["name"] == new_name
    # Проверяем, что описание компании поменялось
    assert edited["description"] == new_descr

#Удаление
def test_delete():
    name = "Company to be deleted"
    descr = "Delete me"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # Обращаемся к компании
    new_company = api.get_company(new_id)
    # Проверим название, описание и статус компании:
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["is_active"] is True

    #Получаем список компаний и сохраняем его длинну
    body = api.get_company_list()
    len_before = len(body)

    #Удаляем компанию
    api.delete_company(new_id)

    # Проверяем что спсок компаний меньше на 1
    body = api.get_company_list()
    len_after = len(body)
    assert len_before- len_after == 1

    #Проверяем что удаленная компания не находится по id
    deleted = api.get_company(new_id)
    assert deleted['detail'] == 'Компания не найдена'


#Деактивация и активация
def test_deactive_and_activate_back():
    # Создаем компанию
    name = "Company to be deactivated"
    result = api.create_company(name)
    new_id = result["id"]

    # Обновляем статус
    api.set_active_state(new_id, True)

    # Получаем обновлённые данные (отдельный GET-запрос)
    updated_company = api.get_company(new_id)  # предполагаемый метод

    # Теперь проверяем актуальное состояние
    assert updated_company["is_active"] == True