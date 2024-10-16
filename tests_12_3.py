import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        cls.index = 0

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrew = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(self):
        pass
        # for i, j in self.all_results.items():
        #     print(j)
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        trial = Tournament(90, self.usain, self.nick)
        self.all_results[self.__class__.index] = trial.start()
        self.__class__.index += 1
        last_test = self.all_results[max(self.all_results.keys())]
        name = last_test[max(last_test.keys())]
        self.assertTrue(name == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        trial = Tournament(90, self.andrew, self.nick)
        self.all_results[self.__class__.index] = trial.start()
        self.__class__.index += 1
        last_test = self.all_results[max(self.all_results.keys())]
        name = last_test[max(last_test.keys())]
        self.assertTrue(name == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        trial = Tournament(90, self.usain, self.andrew, self.nick)
        self.all_results[self.__class__.index] = trial.start()
        self.__class__.index += 1
        last_test = self.all_results[max(self.all_results.keys())]
        name = last_test[max(last_test.keys())]
        self.assertTrue(name == 'Ник')

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        chaser = Runner('Jane',5)
        for i in range(10): chaser.run()
        self.assertEqual(chaser.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walker = Runner('John',5)
        for i in range(10): walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        first = Runner('John',5)
        second = Runner('Jane',5)
        for i in range(10): first.run(), second.walk()
        self.assertNotEqual(first.distance, second.distance)