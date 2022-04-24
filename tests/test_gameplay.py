import sys

_path = __file__.replace("/tests/test_gameplay.py", "/sources")
sys.path[0] = _path

import unittest
import os

from gameplay import GamePlay


class TestCaseRun(unittest.TestCase):
    pass
