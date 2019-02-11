import requests
import urllib.request as request

class TogglDetailedApiReader:
    def __init__(self, apiKey, workspaceId):
        self.apiKey = apiKey
        self.workspaceId = workspaceId

    def download(self, startDate, endDate):
        page = 1
        data = []

        while True:
            result = self.downloadPage(startDate, endDate, page)
            #for d in result.data:
            #    data.co
            data.extend(result["data"].copy())
            if (result["per_page"] * page) >= result["total_count"]:
                break
            else:
                page += 1
        
        return data

    def downloadPage(self, startDate, endDate, page):
        url = "https://toggl.com/reports/api/v2/details"
        params = {
            "workspace_id": self.workspaceId,
            "user_agent": "toggle_to_openair",
            "since": startDate,
            "until": endDate,
            "page": page
        }

        response = requests.get(url, auth=(self.apiKey, 'api_token'), params=params)

        return response.json()