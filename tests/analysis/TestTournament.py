from tourny.structure.foundation import *
from tourny.structure.teams import *
from tourny.analysis.tournament import *
import numpy as np

import unittest as ut

class TestTournament(ut.TestCase):
    def setUp(self):

        self.teamName = "Toronto Maple Leafs"

        self.list32 = hockey
        
        self.tourny = Tournament(self.list32)
        self.tourny.runTournament()
        self.teamNames = getTeamNames(self.tourny)

    # Not needed
    def tearDown(self):
        pass
        
    # Not needed
    @classmethod
    def setUpClass(cls):
        pass
        
    # Not needed
    @classmethod
    def tearDownClass(cls):
        pass
    
    def test_helper_functions(self):

        initialDict = initializeWinCounts(self.teamNames)
        startingZeros = np.all(np.array(list(initialDict.values())) == 0)
        
        self.assertEqual(len(self.teamNames), 32)
        self.assertEqual(type(initialDict), dict)
        self.assertTrue(startingZeros)
        self.assertEqual(set(self.teamNames), set(list(initialDict.keys())))

    def test_get_winner_probabilities(self):
        winnerProbs = getWinnerProbabilities(self.tourny)

        self.assertEqual(len(list(winnerProbs.keys())), len(self.teamNames))
        self.assertEqual(set(list(winnerProbs.keys())), set(self.teamNames))
        self.assertTrue(all(winnerProbs.values()) and len(list(winnerProbs.values())) == len(self.teamNames))
        self.assertTrue(int(sum(list(winnerProbs.values()))) == 1)