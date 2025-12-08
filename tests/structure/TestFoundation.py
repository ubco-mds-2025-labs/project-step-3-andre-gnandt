from tourny.structure.foundation import *
from tourny.structure.teams import *
import random

import unittest as ut

class TestFoundation(ut.TestCase) : #test class
    def setUp(self):

        self.list32_sorted = hockey
        self.list32_unsorted = random.sample(self.list32_sorted, k=len(self.list32_sorted))

        self.tourny_random = Tournament(self.list32_unsorted, "random")
        self.tourny_similar = Tournament(self.list32_unsorted, "similar")
        self.tourny_opposite = Tournament(self.list32_unsorted, "opposite")

        self.tourny_random.runTournament()
        self.tourny_similar.runTournament()
        self.tourny_opposite.runTournament()

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
    
    def test_completedTournament_random(self):

        self.assertTrue(False)

        numRounds = len(self.tourny_random.rounds)

        numMatches0 = len(self.tourny_random.rounds[0].matches)
        numMatches1 = len(self.tourny_random.rounds[1].matches)
        numMatches2 = len(self.tourny_random.rounds[2].matches)
        numMatches3 = len(self.tourny_random.rounds[3].matches)
        numMatches4 = len(self.tourny_random.rounds[4].matches)
        
        self.assertEqual(numRounds, 5)

        self.assertEqual(numMatches0, 16)
        self.assertEqual(numMatches1, 8)
        self.assertEqual(numMatches2, 4)
        self.assertEqual(numMatches3, 2)
        self.assertEqual(numMatches4, 1)

    def test_completedTournament_similar(self):

        numRounds = len(self.tourny_similar.rounds)

        numMatches0 = len(self.tourny_similar.rounds[0].matches)
        numMatches1 = len(self.tourny_similar.rounds[1].matches)
        numMatches2 = len(self.tourny_similar.rounds[2].matches)
        numMatches3 = len(self.tourny_similar.rounds[3].matches)
        numMatches4 = len(self.tourny_similar.rounds[4].matches)
        
        self.assertEqual(numRounds, 5)

        self.assertEqual(numMatches0, 16)
        self.assertEqual(numMatches1, 8)
        self.assertEqual(numMatches2, 4)
        self.assertEqual(numMatches3, 2)
        self.assertEqual(numMatches4, 1)

    def test_completedTournament_opposite(self):

        numRounds = len(self.tourny_random.rounds)

        numMatches0 = len(self.tourny_opposite.rounds[0].matches)
        numMatches1 = len(self.tourny_opposite.rounds[1].matches)
        numMatches2 = len(self.tourny_opposite.rounds[2].matches)
        numMatches3 = len(self.tourny_opposite.rounds[3].matches)
        numMatches4 = len(self.tourny_opposite.rounds[4].matches)
        
        self.assertEqual(numRounds, 5)

        self.assertEqual(numMatches0, 16)
        self.assertEqual(numMatches1, 8)
        self.assertEqual(numMatches2, 4)
        self.assertEqual(numMatches3, 2)
        self.assertEqual(numMatches4, 1)

    def test_teamListFunctions(self):

        self.assertEqual(countTeams(self.list32_unsorted), 32)
        self.assertEqual(sortTeamsByQuality(self.list32_unsorted), self.list32_sorted)
        self.assertEqual(getBestTeams(self.list32_unsorted)[0].name, "Toronto Maple Leafs")
        self.assertEqual(getBestTeams(self.list32_sorted)[0].name, "Toronto Maple Leafs")
