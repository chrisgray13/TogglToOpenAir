import unittest
from DailyTimeEntry import DailyTimeEntry
from DailyTimeEntryValidator import DailyTimeEntryValidator

class DailyTimeEntryValidator_Tests(unittest.TestCase):
    def test_isValid_with_valid_data(self):
        entry = DailyTimeEntry("2019-02-17", "client",
                               "project", "description", 0)
        self.assertTrue(DailyTimeEntryValidator().isValid(entry))

    def test_isValid_with_invalid_description(self):
        entry = DailyTimeEntry(None, None, None, None, None)
        self.assertFalse(DailyTimeEntryValidator().isValid(entry))

    def test_isValid_with_invalid_date(self):
        entry = DailyTimeEntry("2019-02", "client",
                               "project", "description", 0)
        self.assertFalse(DailyTimeEntryValidator().isValid(entry))
