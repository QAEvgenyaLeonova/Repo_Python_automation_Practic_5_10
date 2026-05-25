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




