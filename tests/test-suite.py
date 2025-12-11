import unittest
from structure.TestFoundation import TestFoundation
from analysis.TestTournament import TestTournament as TestTournamentAnalysis
from analysis.TestTeam import TestTeam as TestTeamAnalysis
from visualization.TestTournament import TestTournament as TestTournamentViz
from visualization.TestAnalysis import TestAnalysis as TestAnalysisViz

class TestFailure(Exception) :
    def __init__(self):
        pass
    
    def  __str__(self):
        return "Test Error or Failure!"

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
    suite.addTest(TestTournamentViz('test_get_new_file_name'))
    
    suite.addTest(TestAnalysisViz('test_plot_pie_tournament'))
    suite.addTest(TestAnalysisViz('test_plot_pie_team'))

    runner = unittest.TextTestRunner()
    results = runner.run(suite)
    print(results)

    if not results.wasSuccessful() or len(results.errors) > 0 or len(results.failures) > 0:
            raise TestFailure()

test_suite()
