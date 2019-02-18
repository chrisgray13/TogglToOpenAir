import unittest
from TogglDetailedCsvParser import TogglDetailedCsvParser
from DailyTimeEntryValidator import DailyTimeEntryValidator

class TogglDetailedCsvParser_Tests(unittest.TestCase):
    def test_parse_with_valid_data(self):
        parsedEntry = TogglDetailedCsvParser(DailyTimeEntryValidator()).parse(
            "User,Email,client,project,Task,description,Billable,2004-02-28,Start time,End date,End time,1:30:00,Tags,Amount ()")

        self.assertEqual(parsedEntry.date, "2004-02-28")
        self.assertEqual(parsedEntry.client, "client")
        self.assertEqual(parsedEntry.project, "project")
        self.assertEqual(parsedEntry.description, "description")
        self.assertEqual(parsedEntry.duration, 1.5)

    def test_parse_with_too_many_values(self):
        with self.assertRaises(Exception):
            TogglDetailedCsvParser(DailyTimeEntryValidator()).parse(
                "User,Email,Client,Project,Task,Description,Billable,Start date,Start time,End date,End time,Duration,Tags,Amount (),One More")

    def test_parse_with_too_few_values(self):
        with self.assertRaises(Exception):
            TogglDetailedCsvParser(DailyTimeEntryValidator()).parse(
                "User,Email,Client,Project,Task,Description,Billable,Start date,Start time,End date,End time,Duration,Tags")

    def test_parse_with_invalid_description(self):
        with self.assertRaises(Exception):
            TogglDetailedCsvParser(DailyTimeEntryValidator()).parse(
                "User,Email,client,project,Task,,Billable,2004-02-28,Start time,End date,End time,1:00:00,Tags,Amount ()")

    def test_parse_with_invalid_date(self):
        with self.assertRaises(Exception):
            TogglDetailedCsvParser(DailyTimeEntryValidator()).parse(
                "User,Email,client,project,Task,description,Billable,2004-02,Start time,End date,End time,1:00:00,Tags,Amount ()")

    def test_parse_with_invalid_duration(self):
        with self.assertRaises(ValueError):
            TogglDetailedCsvParser(DailyTimeEntryValidator()).parse(
                "User,Email,client,project,Task,description,Billable,2004-02-28,Start time,End date,End time,1:00,Tags,Amount ()")
