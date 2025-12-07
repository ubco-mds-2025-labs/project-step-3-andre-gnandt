import glob, re
import random
from datetime import datetime
from tourny.structure.foundation import *
from tourny.structure.teams import *
from tourny.visualization.tournament import *

import unittest as ut

class TestTournament(ut.TestCase):

    def setUp(self):
        self.edges = []

    # Not needed
    def tearDown(self):
        pass
        
    # Not needed
    @classmethod
    def setUpClass(cls):
        cls.tourny = Tournament(chess)
        cls.tourny.runTournament()
        
    # Not needed
    @classmethod
    def tearDownClass(cls):
        pass

    def test_append_edge(self) :

        previousMatch = self.tourny.rounds[0].matches[0]
        newMatch = self.tourny.rounds[1].matches[0]
        newMatchTeam1 = newMatch.teams[0].name
        newMatchTeam2 = newMatch.teams[1].name

        appendEdge(self.edges, previousMatch, newMatch)

        self.assertEqual(len(self.edges), 1)
        self.assertEqual(len(self.edges[0]), 3)
        self.assertEqual(self.edges[0][1], newMatchTeam1+" vs "+newMatchTeam2)
        self.assertEqual(self.edges[0][2]["label"], "Winner: "+previousMatch.winner.name)


    def test_add_round_edges(self) :

        addRoundEdges(self.edges, self.tourny.rounds[1], self.tourny.rounds[0])
        self.assertEqual(len(self.edges), 4)
        
        name = self.edges[0][1].split(" vs ")[0]
        self.assertTrue(self.tourny.rounds[1].matches[0].teams[0].name == name or self.tourny.rounds[1].matches[0].teams[1].name == name 
            or self.tourny.rounds[1].matches[1].teams[0].name == name or self.tourny.rounds[1].matches[1].teams[1].name == name)
        
        name = self.edges[2][1].split(" vs ")[0]
        self.assertTrue(self.tourny.rounds[1].matches[0].teams[0].name == name or self.tourny.rounds[1].matches[0].teams[1].name == name or
            self.tourny.rounds[1].matches[1].teams[0].name == name or self.tourny.rounds[1].matches[1].teams[1].name == name)
        
        addRoundEdges(self.edges, self.tourny.rounds[2], self.tourny.rounds[1])
        self.assertEqual(len(self.edges), 6)
        

        
