import requests
import json


class ProjectAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

    def create_project(self, title, users):
        url = f"{self.base_url}/api-v2/projects"
        payload = {
            "title": title,
            "users": users
        }

        response = requests.post(
            url=url,
            headers=self.headers,
            data=json.dumps(payload)
        )
        return response
