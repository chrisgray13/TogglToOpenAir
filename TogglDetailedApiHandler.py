from datetime import datetime, timedelta
from TogglDetailedApiReader import TogglDetailedApiReader
from TogglDetailedApiMapper import TogglDetailedApiMapper
from TogglWorkspaceDefaulter import TogglWorkspaceDefaulter

class TogglDetailedApiHandler:
    def handle(self, startDate, apiKey, workspaceId=""):
        if len(workspaceId) == 0:
            workspaceId = TogglWorkspaceDefaulter().get(apiKey)

        endDate = (datetime.strptime(startDate, "%Y-%m-%d") + timedelta(6)).date().isoformat()

        print("\nGetting data for => ", apiKey, workspaceId, startDate, endDate)

        tempEntries = TogglDetailedApiReader(apiKey, workspaceId).get(startDate, endDate)
        if len(tempEntries) == 0:
            raise Exception("Unable to get data for => ", apiKey, workspaceId, startDate, endDate)
        else:
            mapper = TogglDetailedApiMapper()

            return list(map(lambda entry: mapper.map(entry), tempEntries))
