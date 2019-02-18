import unittest
from DailyTimeEntryExtensions import roundDuration, getDay, getDayOfTheWeek

class DailyTimeEntryExtensions_Tests(unittest.TestCase):
    def test_roundDuration_rounds_up_when_above_halfway(self):
        self.assertEqual(roundDuration(1.376), 1.5)

    def test_roundDuration_rounds_up_when_equal_to_halfway(self):
        self.assertEqual(roundDuration(1.375), 1.5)

    def test_roundDuration_rounds_down_when_below_halfway(self):
        self.assertEqual(roundDuration(1.374), 1.25)

    def test_getDay_with_valid_date_gets_day(self):
        self.assertEqual(getDay("2004-02-28"), 28)

    def test_getDay_with_invalid_date_gets_error(self):
        with self.assertRaises(ValueError):
            getDay("2004-02-31")

    def test_getDayOfTheWeek_with_valid_date_and_default_sundayPosition(self):
        self.assertEqual(getDayOfTheWeek("2004-02-28"), 7)

    def test_getDayOfTheWeek_with_valid_date_and_sundayPosition_equal_to_7(self):
        self.assertEqual(getDayOfTheWeek("2004-02-28", 7), 6)

    def test_getDayOfTheWeek_with_valid_date_and_sundayPosition_equal_to_3(self):
        self.assertEqual(getDayOfTheWeek("2004-02-28", 3), 2)

    def test_getDayOfTheWeek_with_invalid_date(self):
        with self.assertRaises(ValueError):
            getDayOfTheWeek("2004-02-31")

    def test_getDayOfTheWeek_with_sundayPosition_below_1(self):
        with self.assertRaises(ValueError):
            getDayOfTheWeek("2004-02-28", 0)

    def test_getDayOfTheWeek_with_sundayPosition_above_7(self):
        with self.assertRaises(ValueError):
            getDayOfTheWeek("2004-02-28", 8)