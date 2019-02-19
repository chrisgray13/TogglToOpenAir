@ECHO OFF
CD /d "%~dp0"

SET ApiKey=3023c97c6b35259823d988083a5bc82e
SET WorkspaceId=
SET PythonPath=C:\Users\cgray\.virtualenvs\Timesheet-TfBeefbu\Scripts

IF "%~1"=="" (
    GOTO DownloadData
) ELSE (
    GOTO ParseData
)

:ParseData
%PythonPath%\python TogglReportParser.py -f %1

GOTO End


:DownloadData
SET /P StartDate=What is the starting date of the timesheet you would like to create in YYYY-MM-DD format?  

%PythonPath%\python TogglReportParser.py -d %StartDate% %ApiKey% %WorkspaceId%

GOTO End


:End
PAUSE