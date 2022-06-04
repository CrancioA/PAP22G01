import unittest
from exam import TimeZoneCompare


class TestAreaFunction(unittest.TestCase):

    def test_get_number_1(self):
        self.assertNotEqual(TimeZoneCompare.get_number_1(600), 45)


if __name__ == "__main__":
    unittest.main()
