class TogglDetailedCsvReader:
    def readData(self, filename):
        entries = []

        with open(filename) as f:
            entries = list(map(lambda line: line, f))

        return entries
