class TogglDetailedAggregator:
    def __init__(self, entryKeyGenerator):
        self.entryKeyGenerator = entryKeyGenerator

    def aggregate(self, entries):
        aggregate = dict()

        for entry in entries:
            entryKey = self.entryKeyGenerator.generate(entry)
            if entryKey in aggregate:
                tempentries = aggregate[entryKey]

                if entry.date in tempentries:
                    tempentry = tempentries[entry.date]

                    # Only add new descriptions
                    if tempentry.description.find(entry.description) == -1: # Not found
                        tempentry.description = tempentry.description + ", " + entry.description

                    tempentry.duration = tempentry.duration + entry.duration

                    tempentries[entry.date] = tempentry
                    aggregate[entryKey] = tempentries
                else:
                    tempentries[entry.date] = entry
                    aggregate[entryKey] = tempentries
            else:
                aggregate[entryKey] = {entry.date: entry}
            
        return aggregate
