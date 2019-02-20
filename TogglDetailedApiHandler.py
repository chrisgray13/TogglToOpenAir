class TogglDetailedApiHandler:
    def __init__(self, detailedReader, detailedMapper):
        self.detailedReader = detailedReader
        self.detailedMapper = detailedMapper

    def handle(self, startDate, endDate):
        tempEntries = self.detailedReader.get(startDate, endDate)
        if len(tempEntries) == 0:
            raise Exception("Unable to get data for => ", startDate, endDate)
        else:
            return list(map(lambda entry: self.detailedMapper.map(entry), tempEntries))
