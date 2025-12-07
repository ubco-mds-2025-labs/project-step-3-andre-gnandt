import unittest
from tests.structure.TestFoundation import TestFoundation
from tests.analysis.TestTournament import TestTournament as TestTournamentAnalysis
from tests.analysis.TestTeam import TestTeam as TestTeamAnalysis
from tests.visualization.TestTournament import TestTournament as TestTournamentViz
from tests.visualization.TestAnalysis import TestAnalysis as TestAnalysisViz

def test_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    
    suite.addTest(TestFoundation('test_completedTournament_random'))
    suite.addTest(TestFoundation('test_completedTournament_similar'))
    suite.addTest(TestFoundation('test_completedTournament_opposite'))
    suite.addTest(TestFoundation('test_teamListFunctions'))

    suite.addTest(TestTournamentAnalysis('test_helper_functions'))
    suite.addTest(TestTournamentAnalysis('test_get_winner_probabilities'))
    
    suite.addTest(TestTeamAnalysis('test_helper_functions'))
    suite.addTest(TestTeamAnalysis('test_get_round_probabilities'))
    
    suite.addTest(TestTournamentViz('test_add_round_edges'))
    suite.addTest(TestTournamentViz('test_append_edge'))
    
    suite.addTest(TestAnalysisViz('test_plot_pie_tournament'))
    suite.addTest(TestAnalysisViz('test_plot_pie_team'))

    runner = unittest.TextTestRunner()
    print(runner.run(suite))

test_suite()
