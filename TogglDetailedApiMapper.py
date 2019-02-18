from DailyTimeEntry import DailyTimeEntry

class TogglDetailedApiMapper:
    def __init__(self, entryValidator):
        self.entryValidator = entryValidator

    def map(self, entry):
        mappedEntry = DailyTimeEntry(
            entry["start"][0:10],
            entry["client"],
            entry["project"],
            entry["description"],
            float(entry["dur"]) / 3600000.0)  # 60 (mins) * 60 (secs) * 1000 (ms)
        if self.entryValidator.isValid(mappedEntry):
            return mappedEntry
        else:
            raise Exception("Invalid time entry => ", mappedEntry)
