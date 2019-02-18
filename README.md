# TogglToOpenAir
This provides a way to create a timesheet in OpenAir from Toggl

Pre-requisites:
This requires an installation of Python (https://www.python.org/downloads/).  You may also have to manually install requests:  pip install requests

To use:

Option A (easiest):
1) Modify the Run.bat to specify:
    - your Toggl API key--this can be found at the bottom of https://toggl.com/app/profile
    - the path containing Python
2) Double-click the Run.bat
3) Follow the instructions on the conosole

Option 2:
1) Modify the Run.bat to specify the path containing Python
2) Download a week's worth of time entries--starting on Monday--from Toggl as a Detailed report
3) Drag and drop the downloaded .csv onto the Run.bat
4) Follow the instructions on the console
