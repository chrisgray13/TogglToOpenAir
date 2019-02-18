class DailyTimeEntryKeyGenerator:
    def generate(self, entry):
        return entry.client + "|" + entry.project