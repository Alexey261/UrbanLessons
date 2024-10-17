import unittest
from rt_with_exceptions import Runner
import logging


class RunnerTest(unittest.TestCase):

    def test_run(self):
        try:
            chaser = Runner(2)
            for i in range(10): chaser.run()
            self.assertEqual(chaser.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner')
            self.assertTrue(False)

    def test_walk(self):
        try:
            walker = Runner('John', -5)
            for i in range(10): walker.walk()
            self.assertEqual(walker.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning('Неверная скорость для Runner')
            self.assertTrue(False)


log_handler = logging.FileHandler(filename='runner_tests.log', mode='w', encoding='utf-8')  # I am using Python 3.8
logging.basicConfig(handlers=[log_handler], level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')


if __name__ == '__main__':
    unittest.main()




