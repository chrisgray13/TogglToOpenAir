import sys
from datetime import datetime, timedelta

from file_handlers.FileLineHandler import FileLineHandler
from TogglDetailedCsvValidator import TogglDetailedCsvValidator
from TogglDetailedCsvParser import TogglDetailedCsvParser
from TogglDetailedCsvHandler import TogglDetailedCsvHandler

from toggl_api.TogglWorkspaceApi import TogglWorkspaceApi
from TogglWorkspaceDefaulter import TogglWorkspaceDefaulter
from toggl_api.TogglDetailedApi import TogglDetailedApi
from TogglDetailedApiMapper import TogglDetailedApiMapper
from TogglDetailedApiHandler import TogglDetailedApiHandler

from DailyTimeEntryKeyGenerator import DailyTimeEntryKeyGenerator
from DailyTimeEntryValidator import DailyTimeEntryValidator
from TogglDetailedAggregator import TogglDetailedAggregator

from OpenAirTimesheetPopulator import OpenAirTimesheetPopulator

entries = []

#Step 0:  Identify method of use
if len(sys.argv) == 3 and sys.argv[1] == "-f":
    #Step 1:  Read and parse the data from the file
    entries = TogglDetailedCsvHandler(
        FileLineHandler(), TogglDetailedCsvValidator(), TogglDetailedCsvParser(DailyTimeEntryValidator())).handle(sys.argv[2])
elif len(sys.argv) == 4 and sys.argv[1] == "-d":
    #Step 1:  Read and parse the data from the Toggl API
    endDate = (datetime.strptime(sys.argv[2], "%Y-%m-%d") +
                timedelta(6)).date().isoformat()

    entries = TogglDetailedApiHandler(
        TogglDetailedApi(sys.argv[3], TogglWorkspaceDefaulter(
            TogglWorkspaceApi(sys.argv[3]))),
        TogglDetailedApiMapper(DailyTimeEntryValidator())).handle(sys.argv[2], endDate)
elif len(sys.argv) == 5 and sys.argv[1] == "-d":
    #Step 1:  Read and parse the data from the Toggl API
    endDate = (datetime.strptime(sys.argv[2], "%Y-%m-%d") +
               timedelta(6)).date().isoformat()

    entries = TogglDetailedApiHandler(
        TogglDetailedApi(sys.argv[3], TogglWorkspaceDefaulter(
            TogglWorkspaceApi(sys.argv[3]), sys.argv[4])),
        TogglDetailedApiMapper(DailyTimeEntryValidator())).handle(sys.argv[2], endDate)
else:
    print("""
Usage:
    -f  [path to a .csv containing Toggl time entries]
    -d  [start date of data to download in YYYY-MM-DD format] [api key for Toggl access] [Optional: workspace id for Toggl access]
""")
    raise Exception("Invalid usage =>", sys.argv)

if len(entries) == 0:
    raise Exception("No time entries")

#Step 2:  Aggregate the time entries by Date, Client, and Project
aggregate = TogglDetailedAggregator(DailyTimeEntryKeyGenerator()).aggregate(entries)

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
