class MockTogglDetailedApi:
    def __init__(self, data):
        self.data = data

    def get(self, startDate, endDate):
        return self.data