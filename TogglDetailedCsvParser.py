from DailyTimeEntry import DailyTimeEntry as DailyTimeEntry

class TogglDetailedCsvParser:
    def parse(self, entry):
        parts = entry.split(",")
        if len(parts) == 14:
            parsedEntry = DailyTimeEntry(parts[7], parts[2], parts[3], parts[5], self.convertDuration(parts[11]))
            if parsedEntry.isValid():
                return parsedEntry
            else:
                raise Exception("Invalid time entry => ",  parsedEntry)
        else:
            raise Exception("Invalid time entry line => ", entry)

    def isHeaderValid(self, header):
        return header == "ï»¿User,Email,Client,Project,Task,Description,Billable,Start date,Start time,End date,End time,Duration,Tags,Amount ()\n"

    def convertDuration(self, duration):
        parts = duration.split(":")

        return float(parts[0]) + (float(parts[1]) / 60.0) + (float(parts[2]) / 3600.0)