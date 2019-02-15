from TogglWorkspaceApiReader import TogglWorkspaceApiReader

class TogglWorkspaceDefaulter:
    def get(self, apiKey):
        workspaces = TogglWorkspaceApiReader(apiKey).get()
        if len(workspaces) == 1:
            return workspaces[0]["id"]
        elif len(workspaces) == 0:
            raise Exception("Unable to find workspaces for API Key => ", apiKey)
        else:
            raise Exception("Unable to determine default workspace.  Please specify from the command-line => ",
                            list(map(lambda w: w["id"], workspaces)))