import unittest
import main


class TestScript(unittest.TestCase):


    def test_input(self):
        answer = 5
        guess = 5
        result = main.run_guess(guess,answer)
        self.assertTrue(result)


    def test_input_incorrect (self):
        result = main.run_guess(5,10)
        self.assertFalse(result)


    def test_input_wrong_number(self):
        result = main.run_guess(5,12)
        self.assertFalse(result)


    def test_input_wrong_type(self):
        result = main.run_guess(5,'ASDF')
        self.assertFalse(result)





if __name__ == '__main__':
    unittest.main();