import unittest
import totest


class TestToTest(unittest.TestCase):

    def test_do_stuff(self):
        test_param = 10
        result = totest.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'asdfasdfasd'
        result = totest.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = totest.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = totest.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff5(self):
        test_param = 0
        result = totest.do_stuff(test_param)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()

