import sys
from datetime import datetime, timedelta
from TogglDetailedCsvReader import TogglDetailedCsvReader
from TogglWorkspaceApiReader import TogglWorkspaceApiReader
from TogglDetailedApiReader import TogglDetailedApiReader
from TogglDetailedApiMapper import TogglDetailedApiMapper
from DailyTimeEntry import DailyTimeEntry
from OpenAirTimesheetPopulator import OpenAirTimesheetPopulator

entries = []

filename = "C:\\Users\\cgray\\Downloads\\Toggl_time_entries_2019-02-04_to_2019-02-10 (1).csv"
apiKey = ""
workspaceId = ""
startDate = "2019-02-04"
endDate = (datetime.strptime(startDate, "%Y-%m-%d") + timedelta(6)).date().isoformat()

#Step 0:  Identify method of use
if len(sys.argv) == 3 and sys.argv[1] == "-f":
    filename = sys.argv[2]

    print("\nParsing data from => ", filename)

    entries = TogglDetailedCsvReader().readData(filename)
elif len(sys.argv) >= 4 and len(sys.argv) <= 5 and sys.argv[1] == "-d":
    apiKey = sys.argv[2]

    if len(sys.argv) == 5:
        workspaceId = sys.argv[3]
        startDate = sys.argv[4]
    else:
        workspaces = TogglWorkspaceApiReader(apiKey).get()
        if len(workspaces) == 1:
            workspaceId = workspaces[0]["id"]
        elif len(workspaces) == 0:
            raise Exception("Unable to find workspaces for API Key => ", apiKey)
        else:
            raise Exception("Unable to determine default workspace.  Please specify from the command-line => ",
                            list(map(lambda w: w["id"], workspaces)))

        startDate = sys.argv[3]

    endDate = (datetime.strptime(startDate, "%Y-%m-%d") + timedelta(6)).date().isoformat()

    print("\nGetting data for => ", apiKey, workspaceId, startDate, endDate)

    tempEntries = TogglDetailedApiReader(apiKey, workspaceId).get(startDate, endDate)
    if len(tempEntries) == 0:
        raise Exception("Unable to get data for => ", apiKey, workspaceId, startDate, endDate)
    else:
        mapper = TogglDetailedApiMapper()
        entries = list(map(lambda entry: mapper.map(entry), tempEntries))
else:
    print("""
Usage:
    -f  [path to a .csv containing Toggl time entries]
    -d  [api key for Toggl access] [workspace id for Toggl access] [start date of data to download in YYYY-MM-DD format]
""")
    raise Exception("Invalid usage =>", sys.argv)

#Step 1:  Read and parse the data from the file
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
print("\n", script)

print("""
**********************************************************************************
 Perform the following steps to create a timesheet:
    1) Copy the above script
    2) Open Chrome and navigate to https://www.openair.com/index.pl
    3) Login
    4) Create a blank timesheet
    5) Press [F12]
    6) Paste the above script into the DevTools Console
    7) Wait about 30 seconds and BAM!!!
**********************************************************************************""")
