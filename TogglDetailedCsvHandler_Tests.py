import unittest
from Mocks.MockTogglDetailedCsvReader import MockTogglDetailedCsvReader
from TogglDetailedCsvValidator import TogglDetailedCsvValidator
from DailyTimeEntryValidator import DailyTimeEntryValidator
from TogglDetailedCsvParser import TogglDetailedCsvParser
from TogglDetailedCsvHandler import TogglDetailedCsvHandler

class TogglDetailedCsvHandler_Tests(unittest.TestCase):
    def test_handle_with_several_entries(self):
        entries = [
            "ï»¿User,Email,Client,Project,Task,Description,Billable,Start date,Start time,End date,End time,Duration,Tags,Amount ()\n",
            "some user,user email adress,some client,project 1,,Meeting,No,2019-02-11,09:15:41,2019-02-11,09:24:58,00:09:17,,",
            "some user,user email adress,some client,project 1,,Email,No,2019-02-11,09:24:58,2019-02-11,09:31:36,00:06:38,,",
            "some user,user email adress,some client,project 2,,Sprint Launch,No,2019-02-11,09:31:43,2019-02-11,10:50:58,01:19:15,,",
            "some user,user email adress,some client,project 3,,Timesheets,No,2019-02-11,10:50:45,2019-02-11,11:32:57,00:42:12,,",
            "some user,user email adress,some client,project 4,,Customer Issue,No,2019-02-11,11:32:58,2019-02-11,11:38:37,00:05:39,,",
            "some user,user email adress,some client,project 3,,Email,No,2019-02-11,11:39:02,2019-02-11,11:43:02,00:04:00,,",
            "some user,user email adress,some client,project 5,,Product Issue,No,2019-02-11,11:43:09,2019-02-11,12:34:50,00:51:41,,",
            "some user,user email adress,some client,project 6,,Helping with Feature,No,2019-02-11,12:34:58,2019-02-11,13:16:49,00:41:51,,"
        ]
        parsedEntries = TogglDetailedCsvHandler(
            MockTogglDetailedCsvReader(entries),
            TogglDetailedCsvValidator(),
            TogglDetailedCsvParser(DailyTimeEntryValidator())).handle("some file path")

        self.assertEqual(len(parsedEntries), 8)

    def test_handle_with_no_entries(self):
        with self.assertRaises(Exception):
            TogglDetailedCsvHandler(
                MockTogglDetailedCsvReader([]),
                TogglDetailedCsvValidator(),
                TogglDetailedCsvParser(DailyTimeEntryValidator())).handle("some file path")

    def test_handle_with_invalid_header(self):
        with self.assertRaises(Exception):
            entries = [
                "some user,user email adress,some client,project 1,,Meeting,No,2019-02-11,09:15:41,2019-02-11,09:24:58,00:09:17,,",
                "some user,user email adress,some client,project 1,,Email,No,2019-02-11,09:24:58,2019-02-11,09:31:36,00:06:38,,"
            ]
            parsedEntries = TogglDetailedCsvHandler(
                MockTogglDetailedCsvReader(entries),
                TogglDetailedCsvValidator(),
                TogglDetailedCsvParser(DailyTimeEntryValidator())).handle("some file path")
