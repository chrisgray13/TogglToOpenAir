from datetime import datetime

class DailyTimeEntryValidator:
    def isValid(self, entry):
        if entry.description == None:
            return False
    
        try:
            datetime.strptime(entry.date, "%Y-%m-%d")
        except ValueError:
            return False

        return True
