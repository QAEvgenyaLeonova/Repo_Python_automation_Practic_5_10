import requests

class CompanyApi:

    def __init__(self, url):
        self.url = url

    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url + '/company/list', params=params_to_add)
        return resp.json()

    def get_token(self, user='harrypotter', password='expelliarmus'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url +  '/auth/login', json=creds)
        return resp.json()['user_token']

    def create_company(self, name, description=''):
        company = {
            'name': name,
            'description': description,
            'is_active': True
        }
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()
        resp = requests.post(self.url +  '/company/create', json=company, headers=my_headers)
        return resp.json()

