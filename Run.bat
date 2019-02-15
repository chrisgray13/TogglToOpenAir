@ECHO OFF
CD /d "%~dp0"

SET ApiKey=
SET WorkspaceId=
SET PythonPath=
SET FileName=%1

IF "%FileName:"=%"=="" (
    GOTO DownloadData
) ELSE (
    GOTO ParseData
)

:ParseData
%PythonPath%\python TogglReportParser.py -f %FileName%

GOTO End


:DownloadData
SET /P StartDate=What is the starting date of the timesheet you would like to create in YYYY-MM-DD format?  

%PythonPath%\python TogglReportParser.py -d %ApiKey% %WorkspaceId% %StartDate%

GOTO End


:End
PAUSE