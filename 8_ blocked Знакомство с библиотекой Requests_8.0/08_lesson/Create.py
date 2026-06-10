import requests

class ProjectAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url.rstrip('/')
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

    def create_project(self, title, users):
        data = {
            'title': title,
            'users': users
        }
        return requests.post(
            f'{self.base_url}/api-v2/projects',
            json=data,
            headers=self.headers,
            timeout=10
        )

    def update_project(self, project_id, title, users):
        data = {
            'title': title,
            'users': users
        }
        return requests.put(
            f'{self.base_url}/api-v2/projects/{project_id}',
            json=data,
            headers=self.headers,
            timeout=10
        )

    def get_project(self, project_id):
        return requests.get(
            f'{self.base_url}/api-v2/projects/{project_id}',
            headers=self.headers,
            timeout=10
        )
