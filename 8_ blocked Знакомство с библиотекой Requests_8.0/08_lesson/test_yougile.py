from http.client import responses

import requests
import json


base_url = 'https://ru.yougile.com'

def test_authorization_yougile():
    creds = {
        "login": "testing.qa@inbox.ru",
        "password": "Asdf!2218"
    }
    response = requests.post(base_url + '/api-v2/auth/companies', json=creds)
    assert response.status_code == 200

def test_company_yougile_all_list():
    creds = {
        "login": "testing.qa@inbox.ru",
        "password": "Asdf!2218"
    }
    response = requests.post(base_url + '/api-v2/auth/companies', json=creds)
    response_body = response.json()
    assert response.status_code == 200

def test_project_yougile_all_list():
