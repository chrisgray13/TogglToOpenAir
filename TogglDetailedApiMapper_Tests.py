import unittest
from TogglDetailedApiMapper import TogglDetailedApiMapper
from DailyTimeEntryValidator import DailyTimeEntryValidator

class TogglDetailedApiMapper_Tests(unittest.TestCase):
    def test_map_with_valid_data(self):
        mappedEntry = TogglDetailedApiMapper(DailyTimeEntryValidator()).map(
            {"start": "2004-02-28", "client": "client", "project": "project", "description": "description", "dur": 3600000})

        self.assertEqual(mappedEntry.date, "2004-02-28")
        self.assertEqual(mappedEntry.client, "client")
        self.assertEqual(mappedEntry.project, "project")
        self.assertEqual(mappedEntry.description, "description")
        self.assertEqual(mappedEntry.duration, 1.0)

    def test_map_with_invalid_description(self):
        with self.assertRaises(Exception):
            TogglDetailedApiMapper(DailyTimeEntryValidator()).map(
                {"start": "2004-02-28", "client": "client", "project": "project", "description": None, "dur": 3600000})

    def test_map_with_invalid_date(self):
        with self.assertRaises(Exception):
            TogglDetailedApiMapper(DailyTimeEntryValidator()).map(
                {"start": "2004-02", "client": "client", "project": "project", "description": "description", "dur": 3600000})

    def test_map_with_missing_data(self):
        with self.assertRaises(KeyError):
            TogglDetailedApiMapper(DailyTimeEntryValidator()).map({})
