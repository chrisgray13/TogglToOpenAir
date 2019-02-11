@ECHO OFF
CD /d "%~dp0"

SET ApiKey=11b33d94b037db95f58d919988ddadff
SET WorkspaceId=3217695
SET PythonPath=C:\Users\cgray\.virtualenvs\Timesheet-TfBeefbu\Scripts

IF "%1"=="" GOTO DownloadData
ELSE GOTO ParseData

:DownloadData
SET /P StartDate=What is the starting date of the timesheet you would like to create in YYYY-MM-DD format?  

%PythonPath%\python TogglReportParser.py -d %ApiKey% %WorkspaceId% %StartDate%

GOTO End


:ParseData
%PythonPath%\python TogglReportParser.py -f %1


:End
PAUSE