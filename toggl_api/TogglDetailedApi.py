import requests

class TogglDetailedApi:
    def __init__(self, apiKey, workspaceDefaulter):
        self.apiKey = apiKey
        self.workspaceDefaulter = workspaceDefaulter

    def get(self, startDate, endDate):
        page = 1
        data = []

        workspaceId = self.workspaceDefaulter.get()

        print("\nGetting data for => ", self.apiKey,
              workspaceId, startDate, endDate)

        while True:
            result = self.getPage(workspaceId, startDate, endDate, page)
            if len(result["data"]) == 0:
                raise Exception("Unable to get data for => ", self.apiKey, workspaceId, startDate, endDate)
            else:
                data.extend(result["data"].copy())
                if (result["per_page"] * page) >= result["total_count"]:
                    break
                else:
                    page += 1
        
        return data

    def getPage(self, workspaceId, startDate, endDate, page):
        url = "https://toggl.com/reports/api/v2/details"
        params = {
            "workspace_id": workspaceId,
            "user_agent": "toggle_to_openair",
            "since": startDate,
            "until": endDate,
            "page": page,
            "order_field": "date",
            "order_desc": "off"
        }

        response = requests.get(url, auth=(self.apiKey, 'api_token'), params=params)
        if response.ok:
            return response.json()
        else:
            raise Exception("{0}: {1} => ".format(response.reason, response.json()["error"]["message"]),
                            self.apiKey, workspaceId, startDate, endDate)
