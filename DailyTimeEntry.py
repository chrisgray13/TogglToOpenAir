class DailyTimeEntry:
    def __init__(self, date, client, project, description, duration):
        self.date = date
        self.client = client or ""
        self.project = project or ""
        self.description = description
        self.duration = duration

    def key(self):
        return self.client + "|" + self.project
    
    def isValid(self):
        return self.description != None