@ECHO OFF
CD /d "%~dp0"

SET ApiKey=
SET WorkspaceId=
SET PythonPath=

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