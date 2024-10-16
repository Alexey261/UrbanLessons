import unittest
import tests_12_3


contest_ts = unittest.TestSuite()
contest_ts.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
contest_ts.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))


ts_runner = unittest.TextTestRunner(verbosity=2)
ts_runner.run(contest_ts)