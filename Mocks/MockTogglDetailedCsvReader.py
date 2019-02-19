class MockTogglDetailedCsvReader:
    def __init__(self, entries):
        self.entries = entries

    def readData(self,filename):
        return self.entries