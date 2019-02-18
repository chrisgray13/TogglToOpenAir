import unittest
from TogglDetailedCsvValidator import TogglDetailedCsvValidator

class TogglDetailedCsvValidator_Tests(unittest.TestCase):
    def test_isHeaderValid_with_valid_data(self):
        self.assertTrue(TogglDetailedCsvValidator().isHeaderValid(
            "ï»¿User,Email,Client,Project,Task,Description,Billable,Start date,Start time,End date,End time,Duration,Tags,Amount ()\n"))

    def test_isHeaderValid_with_invalid_data_missing_weird_beginning(self):
        self.assertFalse(TogglDetailedCsvValidator().isHeaderValid(
            "User,Email,Client,Project,Task,Description,Billable,Start date,Start time,End date,End time,Duration,Tags,Amount ()\n"))

    def test_isHeaderValid_with_invalid_data_missing_newline(self):
        self.assertFalse(TogglDetailedCsvValidator().isHeaderValid(
            "ï»¿User,Email,Client,Project,Task,Description,Billable,Start date,Start time,End date,End time,Duration,Tags,Amount ()"))
