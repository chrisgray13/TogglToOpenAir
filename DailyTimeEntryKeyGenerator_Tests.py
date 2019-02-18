import unittest
from DailyTimeEntry import DailyTimeEntry
from DailyTimeEntryKeyGenerator import DailyTimeEntryKeyGenerator

class DailyTimeEntryKeyGenerator_Tests(unittest.TestCase):
    def test_key(self):
        entry = DailyTimeEntry("2019-02-17", "client",
                               "project", "description", 0)
        self.assertEqual(DailyTimeEntryKeyGenerator().generate(entry), "client|project")