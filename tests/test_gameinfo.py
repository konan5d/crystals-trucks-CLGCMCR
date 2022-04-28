#  import sources.gameinfo as gameinfo
import sys

_path = __file__.replace("/tests/test_gameinfo.py", "/sources")
sys.path[0] = _path

import unittest
import os
from gameinfo import GameInfo, Truck


class TestSaveAction(unittest.TestCase):
    def test_save_actions(self):
        g = GameInfo(1, "test.txt")
        outfile = g.output_filemane  # Init file
        g.save_actions(outfile)  # Save test file
        test = False
        if os.path.exists(outfile):
            out = open(outfile, "r")
            content = out.readlines()
            if content != "":
                test = True
        else:
            test = False
        self.assertEqual(test, True)  # Compare


# class TestCaseGameInfo(unittest.TestCase):
#     def test_parse_trucks(self):
#         gi = gameinfo.GameInfo(1, "instructions.txt")
#         gi.run()
#         parser = gameinfo.Parse(gi.raw_data)
#         self.assertEqual(parser.parse_trucks, 6)


class TestCaseTruck(unittest.TestCase):
    def test_move_return_valid_format(self):
        truck = Truck(1, 0, 0)
        self.assertEqual(truck.action_move(1, 5), "MOVE 1 1 5")

    def test_dig_return_valid_format(self):
        truck = Truck(6, 0, 0)
        truck.pos_x = 4
        truck.pos_y = 5
        self.assertEqual(truck.action_dig(), "DIG 6 4 5")


class TestCaseCrystal(unittest.TestCase):
    def test_is_crystal_available_true(self):
        gi = GameInfo(2, "test.txt")
        gi.init_game_info()
        self.assertEqual(gi.is_crystal_available(0, 1), True)

    def test_is_crystal_available_false(self):
        gi = GameInfo(2, "test.txt")
        gi.init_game_info()
        self.assertEqual(gi.is_crystal_available(0, 0), False)


if __name__ == "__main__":
    unittest.main()
