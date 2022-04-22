import sources.gameinfo as gameinfo
import unittest


# class TestCaseGameInfo(unittest.TestCase):
#     def test_parse_trucks(self):
#         gi = gameinfo.GameInfo(1, "instructions.txt")
#         gi.run()
#         parser = gameinfo.Parse(gi.raw_data)
#         self.assertEqual(parser.parse_trucks, 6)


class TestCaseTruck(unittest.TestCase):
    def test_move_return_valid_format(self):
        truck = gameinfo.Truck(0, 0)
        self.assertEqual(truck.action_move(1, 5), "MOVE 1 5")

    def test_dig_return_valid_format(self):
        truck = gameinfo.Truck(0, 0)
        self.assertEqual(truck.action_dig(4, 5), "DIG 4 5")


if __name__ == "__main__":
    unittest.main()
