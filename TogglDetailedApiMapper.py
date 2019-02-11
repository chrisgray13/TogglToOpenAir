from DailyTimeEntry import DailyTimeEntry

class TogglDetailedApiMapper:
    def map(self, entry):
        mappedEntry = DailyTimeEntry(
            entry["start"][0:10],
            entry["client"],
            entry["project"],
            entry["description"],
            float(entry["dur"]) / 3600000.0)  # 60 (mins) * 60 (secs) * 1000 (ms)
        if mappedEntry.isValid():
            return mappedEntry
        else:
            raise Exception("Invalid time entry => ", mappedEntry)