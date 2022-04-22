#  import sources.gameinfo as gameinfo

import unittest
import os
from xmlrpc.client import boolean

from sources.gameinfo import GameInfo as gi


class GameInfo_Tests(unittest.TestCase):
    def test_save_actions(self):
        g = gi()
        outfile = g.actionsFileName  # Init file
        test_content = ["content"]  # Init content
        g.save_actions(outfile, test_content)  # Save test file
        test = False
        if os.path.exists(outfile):
            out = open(outfile, "r")
            content = out.readlines()
            test = True
        else:
            test = False
        self.assertEqual(test, True)  # Compare
