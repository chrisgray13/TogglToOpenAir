from TogglDetailedCsvParser import TogglDetailedCsvParser

class TogglDetailedCsvReader:
    def readData(self, filename):
        entries = []

        with open(filename) as f:
            parser = TogglDetailedCsvParser()

            header = f.readline()
            if not parser.isHeaderValid(header):
                raise Exception("Invalid header row => ", header)

            entries = list(map(lambda line: parser.parse(line), f))
            #for line in f:
            #    entry = parser.parse(line)

        return entries
