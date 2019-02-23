import unittest
from mocks.MockTogglDetailedApi import MockTogglDetailedApi
from DailyTimeEntryValidator import DailyTimeEntryValidator
from TogglDetailedApiMapper import TogglDetailedApiMapper
from TogglDetailedApiHandler import TogglDetailedApiHandler

class TogglDetailedApiHandler_Tests(unittest.TestCase):
    def test_handle_with_several_entries(self):
        entries = [
            {
                "description": "Meeting",
                "start": "2004-02-28T09:15:41-05:00",
                "dur": 557000,
                "client": "client 1",
                "project": "project 1"
            },
            {
                "description": "Email",
                "start": "2004-02-28T09:24:58-05:00",
                "dur": 398000,
                "client": "client 1",
                "project": "project 1"
            },
            {
                "description": "Sprint Launch",
                "start": "2004-02-28T09:31:43-05:00",
                "dur": 4755000,
                "client": "client 1",
                "project": "project 3"
            },
            {
                "description": "Timesheets",
                "start": "2004-02-28T10:50:45-05:00",
                "dur": 2532000,
                "client": "client 1",
                "project": "project 1"
            },
            {
                "description": "Customer Issue",
                "start": "2004-02-28T11:32:58-05:00",
                "dur": 339000,
                "client": "client 1",
                "project": "project 2"
            }
        ]

        mappedEntries = TogglDetailedApiHandler(
            MockTogglDetailedApi(entries),
            TogglDetailedApiMapper(DailyTimeEntryValidator())).handle("2004-02-28", "2004-03-05")

        self.assertEqual(len(mappedEntries), 5)
        self.assertEqual(mappedEntries[0].description, "Meeting")
        self.assertEqual(mappedEntries[1].date, "2004-02-28")
        self.assertEqual(round(mappedEntries[2].duration, 3), 1.321)
        self.assertEqual(mappedEntries[3].client, "client 1")
        self.assertEqual(mappedEntries[4].project, "project 2")

    def test_handle_with_no_entries(self):
        with self.assertRaises(Exception):
            TogglDetailedApiHandler(
                MockTogglDetailedApi([]),
                TogglDetailedApiMapper(DailyTimeEntryValidator())).handle("2004-02-28", "2004-03-05")
