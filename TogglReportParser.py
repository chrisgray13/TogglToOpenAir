from DailyTimeCsvReader import DailyTimeCsvReader
from DailyTimeEntry import DailyTimeEntry
from OpenAirTimesheetPopulator import OpenAirTimesheetPopulator

#Step 1:  Read and parse the data from the file
entries = DailyTimeCsvReader().readData('C:\\Users\\cgray\\Downloads\\Toggl_time_entries_2019-02-04_to_2019-02-10 (1).csv')

if len(entries) == 0:
    raise Exception("No time entries")

#TODO:  Add date validation to ensure it does not span more than 7 days

#Step 2:  Aggregate the time entries by Date, Client, and Project
aggregate = dict()

for entry in entries:
    if entry.key() in aggregate:
        tempentries = aggregate[entry.key()]
        
        if entry.date in tempentries:
            tempentry = tempentries[entry.date]
            
            # Only add new descriptions
            if tempentry.description.find(entry.description) == -1:
                tempentry.description = tempentry.description + ", " + entry.description

            tempentry.duration = tempentry.duration + entry.duration

            tempentries[entry.date] = tempentry
            aggregate[entry.key()] = tempentries
        else:
            tempentries[entry.date] = entry
            aggregate[entry.key()] = tempentries
    else:
        aggregate[entry.key()] = { entry.date: entry }

#Step 3:  Generate the OpenAir timesheet population code
populator = OpenAirTimesheetPopulator()
script = populator.generateTimesheetPopulationScript(aggregate.values())
print(script)