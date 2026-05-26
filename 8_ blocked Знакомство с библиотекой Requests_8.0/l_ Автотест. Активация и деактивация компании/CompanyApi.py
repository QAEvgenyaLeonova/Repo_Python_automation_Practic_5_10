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

    def get_company(self, id):
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()

    def create_company(self, name, description=''):
        company = {
            'name': name,
            'description': description,
            'is_active': True
        }
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()
        resp = requests.post(self.url +  '/company/create', json=company, headers=my_headers)
        return resp.json()\


    def edit_company(self, new_id, new_name, new_description):
        client_token = self.get_token()

        url_with_token = f"{self.url}/company/update/{new_id}?client_token={client_token}"

        company = {
            'name': new_name,
            'description': new_description
        }

        resp = requests.patch(url_with_token, json=company)
        return resp.json()

    def delete_company(self, id):
        client_token = self.get_token()

        url_with_token = f"{self.url}/company/{id}?client_token={client_token}"

        resp = requests.delete(url_with_token)
        return resp.json()

    def set_active_state(self, id, is_active):
        client_token = self.get_token()

        url_with_token = f"{self.url}/company/status_update/{id}?client_token={client_token}"
        resp = requests.patch(url_with_token,
                              json={"is_active": is_active})
        return resp.json()



