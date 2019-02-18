class DailyTimeEntry:
    def __init__(self, date, client, project, description, duration):
        self.date = date
        self.client = client or ""
        self.project = project or ""
        self.description = description
        self.duration = duration