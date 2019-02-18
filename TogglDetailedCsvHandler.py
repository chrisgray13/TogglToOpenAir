class TogglDetailedCsvHandler:
    def __init__(self, detailedReader, detailedParser):
        self.detailedReader = detailedReader
        self.detailedParser = detailedParser

    def handle(self, filename):
        print("\nParsing data from => ", filename)

        tempEntries = self.detailedReader.readData(filename)
        if len(tempEntries) == 0:
            raise Exception("Unable to get data for => ", filename)
        else:
            header = tempEntries[0]
            if self.detailedParser.isHeaderValid(header):
                return list(map(lambda line: self.detailedParser.parse(line), tempEntries[1:]))
            else:
                raise Exception("Invalid header row => ", header)