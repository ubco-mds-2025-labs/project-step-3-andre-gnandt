from tourny.structure.foundation import *
from tourny.structure.teams import *
from tourny.analysis.team import *

import unittest as ut

class TestTeam(ut.TestCase):
    
    def setUp(self):

        self.teamName = "Toronto Maple Leafs"

        self.list32 = hockey
        
        self.tourny = Tournament(self.list32)
        self.tourny.runTournament()

        self.roundKeys = getRoundKeys(self.tourny)

    # Not needed
    def tearDown(self):
        pass
        
    # Not needed
    @classmethod
    def tearDownClass(cls):
        pass
        
    # Not needed
    @classmethod
    def setUpClass(cls):
        pass
    
    def test_helper_functions(self):

        firstRoundWinners = getRoundWinnerNames(self.tourny.rounds[0])
        lastRoundWinners = getRoundWinnerNames(self.tourny.rounds[-1])
        secondLastRoundWinners = getRoundWinnerNames(self.tourny.rounds[-2])

        self.assertEqual(len(self.roundKeys), 6)
        self.assertEqual(len(firstRoundWinners), 16)
        self.assertEqual(len(lastRoundWinners), 1)
        self.assertEqual(len(secondLastRoundWinners), 2)

    def test_get_round_probabilities(self):

        roundProbs = getRoundProbablities(self.tourny, self.teamName)

        self.assertEqual(len(list(roundProbs.keys())), len(self.roundKeys))
        self.assertEqual(list(roundProbs.keys()), self.roundKeys)
        self.assertTrue(all(roundProbs.values()))
        self.assertEqual(int(sum(list(roundProbs.values()))), 1)