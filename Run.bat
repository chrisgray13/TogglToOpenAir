@ECHO OFF
CD /d "%~dp0"

SET ApiKey=
SET WorkspaceId=
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