import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from functions.rmse import *

class TestRMSE(unittest.TestCase):

    def test_example(self):
        predictions = [1, 2, 3, 4]
        obervations = [4, 3, 2, 1]
        self.assertAlmostEqual(rmse(predictions,obervations), 2.2361, 3)

def suite():
    suite = unittest.makeSuite(TestRMSE, 'test')
    return suite

def run():
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite())

if __name__ == "__main__":
    run()
