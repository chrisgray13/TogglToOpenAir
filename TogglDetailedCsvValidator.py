class TogglDetailedCsvValidator:
    def isHeaderValid(self, header):
        return header == "ï»¿User,Email,Client,Project,Task,Description,Billable,Start date,Start time,End date,End time,Duration,Tags,Amount ()\n"