#  import sources.gameinfo as gameinfo

import unittest

from sources.gameinfo import GameInfo as gi


class GameInfo_Tests(unittest.TestCase):

    def test_save_actions(self):
        outfile = gi.actionsFileName        # Init file
        test_content = ["content"]          # Init content
        gi.save_actions(outfile,test_content)      # Save test file
        outfile.seek(0)
        content = outfile.read()        # Reading of test file
        self.assertEqual(content,"content")        # Compare data with
