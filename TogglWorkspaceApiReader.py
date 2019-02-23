import requests

class TogglWorkspaceApiReader:
    def __init__(self, apiKey):
        self.apiKey = apiKey
    
    def get(self):
        url = "https://www.toggl.com/api/v8/workspaces"

        response = requests.get(url, auth=(
            self.apiKey, 'api_token'))

        return response.json()

    def getClients(self, workspaceId):
        url = "https://www.toggl.com/api/v8/workspaces/{0}/clients".format(
            workspaceId)

        response = requests.get(url, auth=(
            self.apiKey, 'api_token'))

        return response.json()

    def getProjects(self, workspaceId):
        url = "https://www.toggl.com/api/v8/workspaces/{0}/projects".format(workspaceId)

        response = requests.get(url, auth=(
            self.apiKey, 'api_token'))

        return response.json()

    def getTasks(self, workspaceId):
        url = "https://www.toggl.com/api/v8/workspaces/{0}/tasks".format(
            workspaceId)

        response = requests.get(url, auth=(
            self.apiKey, 'api_token'))

        return response.json()
