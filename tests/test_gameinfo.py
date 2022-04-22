import sources.gameinfo as gameinfo
import unittest


class TestCaseGameInfo(unittest.TestCase):
    def test_parse_trucks(self):
        gi = gameinfo.GameInfo(1, "instructions.txt")
        gi.run()
        parser = gameinfo.Parse(gi.raw_data)
        self.assertEqual(parser.parse_trucks, 6)


if __name__ == "__main__":
    unittest.main()
