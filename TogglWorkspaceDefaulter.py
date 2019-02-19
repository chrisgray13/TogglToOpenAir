class TogglWorkspaceDefaulter:
    def __init__(self, workspaceReader, defaultWorkspaceId = None):
        self.workspaceReader = workspaceReader
        self.workspaceId = defaultWorkspaceId

    def get(self):
        if self.workspaceId == None:
            workspaces = self.workspaceReader.get()
            if len(workspaces) == 1:
                self.workspaceId = workspaces[0]["id"]
                return self.workspaceId
            elif len(workspaces) == 0:
                raise Exception("Unable to find workspaces")
            else:
                raise Exception("Unable to determine default workspace.  Please specify from the command-line => ",
                                list(map(lambda w: w["id"], workspaces)))
        else:
            return self.workspaceId
