class TogglDetailedAggregator:
    def aggregate(self, entries):
        aggregate = dict()

        for entry in entries:
            if entry.key() in aggregate:
                tempentries = aggregate[entry.key()]

                if entry.date in tempentries:
                    tempentry = tempentries[entry.date]

                    # Only add new descriptions
                    if tempentry.description.find(entry.description) == -1: # Not found
                        tempentry.description = tempentry.description + ", " + entry.description

                    tempentry.duration = tempentry.duration + entry.duration

                    tempentries[entry.date] = tempentry
                    aggregate[entry.key()] = tempentries
                else:
                    tempentries[entry.date] = entry
                    aggregate[entry.key()] = tempentries
            else:
                aggregate[entry.key()] = {entry.date: entry}
            
        return aggregate