import requests

class TogglWorkspaceApiReader:
    def __init__(self, apiKey):
        self.apiKey = apiKey
    
    def get(self):
        url = "https://www.toggl.com/api/v8/workspaces"

        response = requests.get(url, auth=(
            self.apiKey, 'api_token'))

        return response.json()
