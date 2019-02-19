class MockTogglWorkspaceApiReader:
    def __init__(self, workspaces):
        self.workspaces = workspaces

    def get(self):
        return self.workspaces
