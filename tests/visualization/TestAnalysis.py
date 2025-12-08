import glob, re
from tourny.structure.foundation import *
from tourny.structure.teams import *
from tourny.visualization.analysis import *
from tourny.analysis.tournament import *
from tourny.analysis.team import *

import unittest as ut

class TestAnalysis(ut.TestCase):

    def setUp(self):
        self.tourny = Tournament(chess)

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

    def test_plot_pie_tournament(self) :

        winnerProbabilities = getWinnerProbabilities(self.tourny)
        self.assertEqual(sum(list(winnerProbabilities.values())),1)
        self.assertTrue(len(list(winnerProbabilities.values())), len(chess))

        plotPieTournament(winnerProbabilities, None, "TOURNTEST")
        self.assertTrue(len(glob.glob("TOURNTEST.svg")) >= 1)

        plotPieTournament(winnerProbabilities, self.tourny.pairingType)
        self.assertTrue(len(glob.glob("pieTournament*.svg")) > 0)

        pieTournament(self.tourny, "TOURNTEST2")
        self.assertTrue(len(glob.glob("TOURNTEST2.svg")) >= 1)

    def test_plot_pie_team(self) :
        teamName = 'Fabiano Caruana'

        roundProbabilities = getRoundProbablities(self.tourny, teamName)
        self.assertEqual(sum(list(roundProbabilities.values())),1)
        self.assertTrue(len(list(roundProbabilities.values())), len(self.tourny.rounds))

        plotPieTeam(roundProbabilities, teamName, None, "PIETEST")
        self.assertTrue(len(glob.glob("PIETEST.svg")) >= 1)

        plotPieTeam(roundProbabilities, teamName, self.tourny.pairingType)
        self.assertTrue(len(glob.glob("pieTeam*.svg")) > 0)

        pieTeam(self.tourny, 'Fabiano Caruana', "PIETEST2")
        self.assertTrue(len(glob.glob("PIETEST2.svg")) >= 1)
        

        
