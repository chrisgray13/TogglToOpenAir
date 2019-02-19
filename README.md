# TogglToOpenAir
This provides a way to create a timesheet in OpenAir based on tracking data in Toggl

#### Pre-requisites:
This requires the following to be useful:
- An installation of [Python](https://www.python.org/downloads/).  You may also have to manually install requests:  `pip install requests`
- [Toggl](https://toggl.com/) for tracking your time
- [OpenAir](https://www.openair.com/index.pl) for submitting a timesheet

#### To use\*:

###### Option A (easiest):
1) Modify the Run.bat to specify:
    - your Toggl API key--this can be found at the bottom of [Toggl Profile](https://toggl.com/app/profile)
    - the path containing Python
2) Double-click the Run.bat
3) Follow the instructions on the conosole

###### Option 2:
1) Modify the Run.bat to specify the path containing Python
2) Download a week's worth of time entries--starting on Monday--from Toggl as a [Detailed report](https://toggl.com/app/reports/detailed)
3) Drag and drop the downloaded .csv onto the Run.bat
4) Follow the instructions on the console

**_\*These options depend on capturing time with Toggl_**
