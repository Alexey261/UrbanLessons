import unittest
from runner_and_tournament import Runner, Tournament

""" БОЛЬШОЙ ВОПРОС:
    Если каждый тест-метод запускается в отдельном экземпляре класса TournamentTest, что подтверждается обнулением
    переменной index (отсюда self.__class__.index += 1), то почему словарь all_results не 'обнуляется', а сохраняет
    в себе значения предыдущих тестов, хотя оба атрибута одинаково определены в setUpClass (индекс нулевой, а словарь
    пустой)????"""

class TournamentTest(unittest.TestCase):

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
        for i, j in self.all_results.items():
            print(j)

    def test_1(self):
        trial = Tournament(90, self.usain, self.nick)
        self.all_results[self.__class__.index] = trial.start()
        self.__class__.index += 1
        last_test = self.all_results[max(self.all_results.keys())]
        name = last_test[max(last_test.keys())]
        self.assertTrue(name == 'Ник')

    def test_2(self):
        trial = Tournament(90, self.andrew, self.nick)
        self.all_results[self.__class__.index] = trial.start()
        self.__class__.index += 1
        last_test = self.all_results[max(self.all_results.keys())]
        name = last_test[max(last_test.keys())]
        self.assertTrue(name == 'Ник')

    def test_3(self):
        trial = Tournament(90, self.usain, self.andrew, self.nick)
        self.all_results[self.__class__.index] = trial.start()
        self.__class__.index += 1
        last_test = self.all_results[max(self.all_results.keys())]
        name = last_test[max(last_test.keys())]
        self.assertTrue(name == 'Ник')


if __name__ == '__main__':
    unittest.main()
