import glob
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
        
    def test_get_new_file_name(self):
        svg_content = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg width="100%" height="100%" viewBox="0 0 100 100" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <!-- Add your SVG elements here -->
        </svg>"""

        titlePrefix = ""
        chars = ['a','b', 'c', '4', '5', 't', 'q', 'z']
        length = random.randint(1,10)
        i = 0
        while i < length :
            titlePrefix = titlePrefix+str(random.choice(chars))
            i=i+1

        greatestTitle = titlePrefix+"-"+datetime.now().strftime("%Y-%m-%d")
        fullPrefix = greatestTitle
        fileCount = 0
        if(len(glob.glob(greatestTitle+".svg")) >= 1) :
            possibleFilesList = glob.glob(greatestTitle+"-?*.svg")
            integerList = []
            for fileName in possibleFilesList :
                if re.fullmatch(rf"{greatestTitle}-[0-9]+.svg", fileName):
                    integerList.append(int(fileName.split("-")[4].split(".")[0]))

            if len(integerList) < 1 :
                greatestTitle =  greatestTitle+"-1"
                fileCount = 1
            else: 
                greatestTitle = greatestTitle+"-"+str(1+max(integerList))
                fileCount = max(integerList)
        
        self.assertEqual(type(getNewFileName(titlePrefix)), str)
        self.assertTrue(len(getNewFileName(titlePrefix).split('-')) >= 4)
        self.assertEqual(len(getNewFileName(titlePrefix)), len(greatestTitle))
        self.assertEqual(getNewFileName(titlePrefix), greatestTitle)
        
