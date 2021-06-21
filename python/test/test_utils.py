from bark_client import utils
import unittest


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertTrue(utils.is_blank(''))
        self.assertTrue(utils.is_blank(None))
        self.assertFalse('', utils.is_blank('Hello World'))


if __name__ == '__main__':
    unittest.main()
