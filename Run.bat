@ECHO OFF
CD /d "%~dp0"

python TogglReportParser.py -f %1

PAUSE