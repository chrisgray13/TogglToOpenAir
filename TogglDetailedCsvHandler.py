from TogglDetailedCsvReader import TogglDetailedCsvReader
from TogglDetailedCsvParser import TogglDetailedCsvParser


class TogglDetailedCsvHandler:
    def handle(self, filename):
        print("\nParsing data from => ", filename)

        tempEntries = TogglDetailedCsvReader().readData(filename)
        if len(tempEntries) == 0:
            raise Exception("Unable to get data for => ", filename)
        else:
            parser = TogglDetailedCsvParser()

            header = tempEntries[0]
            if parser.isHeaderValid(header):
                return list(map(lambda line: parser.parse(line), tempEntries[1:]))
            else:
                raise Exception("Invalid header row => ", header)