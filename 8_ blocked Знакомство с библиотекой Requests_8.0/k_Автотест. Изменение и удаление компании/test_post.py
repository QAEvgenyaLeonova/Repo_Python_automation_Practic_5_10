import requests
from CompanyApi import CompanyApi

api = CompanyApi('http://5.101.50.27:8000')

def test_get_companies():
    body = api.get_company_list()
    assert len(body) > 0 #== X

def test_get_active_companies():                                         #Получить список всех компаний
    full_list = api.get_company_list()
    filtered_list = api.get_company_list(params_to_add= {'active': True})#Получить список активных компаний
    assert len(full_list) > len(filtered_list)                           #Проверить что список 1 > больше списка 2


def test_add_new():                                                      # Получить количество компаний до создания
    body = api.get_company_list()
    len_before = len(body)

    name = 'Autotest'                                                    # Создать новую компанию
    description = 'Decsr'
    result = api.create_company(name, description)
    new_id = result['is_active']

    body = api.get_company_list()                                         # Получить, количество опять после создания
    len_after = len(body)

    assert  len_after - len_before == 1                                   # Проверить, что стало + 1
    assert body[-1]['name'] == name                                       # Проверить название и описание последней компании и что Active последней компании в списке равен ответу из шага 2
    assert body[-1]['description'] == description
    assert body[-1]['is_active'] == True

def test_get_one_company():
    # Создаем компанию
    name = "VS Code"
    description = "IDE"
    result = api.create_company(name, description)
    new_id = result["id"]

    # Обращаемся к компании
    new_company = api.get_company(new_id)

    # Проверим название, описание и статус новой компании:
    assert new_company["name"] == name
    assert new_company["description"] == description
    assert new_company["is_active"] is True

def test_edit():
    name = 'Company to be edited'
    descr = 'Edit me'
    result = api.create_company(name, descr)
    new_id = result['id']

    new_name = 'Updated2'
    new_descr = '_upd2_'

    edited = api.edit_company(new_id, new_name, new_descr)

    assert edited['name'] == new_name
    assert edited['description'] == new_descr

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

    # Получаем список компаний и сохраняем его длину
    body = api.get_company_list()
    len_before = len(body)

    # Удаляем компанию
    api.delete_company(new_id)

    # Проверяем, что список компаний меньше на 1
    body = api.get_company_list()
    len_after = len(body)
    assert len_before- len_after == 1

    # Проверяем, что удаленная компания не находится по id
    deleted = api.get_company(new_id)
    assert deleted['detail'] == 'Компания не найдена'











