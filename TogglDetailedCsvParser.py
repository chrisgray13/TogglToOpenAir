from DailyTimeEntry import DailyTimeEntry as DailyTimeEntry

class TogglDetailedCsvParser:
    def __init__(self, entryValidator):
        self.entryValidator = entryValidator

    def parse(self, entry):
        parts = entry.split(",")
        if len(parts) == 14:
            try:
                duration = self.convertDuration(parts[11])
            except IndexError:
                raise ValueError("Invalid time entry based on duration => ", entry, parts[11])

            parsedEntry = DailyTimeEntry(parts[7], parts[2], parts[3], parts[5], duration)
            if self.entryValidator.isValid(parsedEntry):
                return parsedEntry
            else:
                raise Exception("Invalid time entry => ",  parsedEntry)
        else:
            raise Exception("Invalid time entry line => ", entry)

    def convertDuration(self, duration):
        parts = duration.split(":")

        return float(parts[0]) + (float(parts[1]) / 60.0) + (float(parts[2]) / 3600.0)
