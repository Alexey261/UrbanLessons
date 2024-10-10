import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):

    def test_run(self):
        chaser = Runner('Jane')
        for i in range(10): chaser.run()
        self.assertEqual(chaser.distance, 100)

    def test_walk(self):
        walker = Runner('John')
        for i in range(10): walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_challenge(self):
        first = Runner('John')
        second = Runner('Jane')
        for i in range(10): first.run(), second.walk()
        self.assertNotEqual(first.distance, second.distance)


if __name__ == '__main__':
    unittest.main()
