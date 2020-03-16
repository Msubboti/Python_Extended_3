from Program_for_Testing import Testing
import unittest


def calculate_number(Number):
    dictionary = Testing(Number)
    banknotes = list(dictionary.keys())
    expected = 0
    for index in banknotes:
        expected += index * dictionary[index]
    return expected


class Test_Correct_Result(unittest.TestCase):

    def setUp(self):                                # This method is started before every test for preparing environment or make settings
        print("Welcome to testing by UnitTest")

    def test_number_2855(self):
        result = calculate_number(2855)
        self.assertEqual(result, 2855)

    @unittest.skipIf(calculate_number(35), "Value 35 is not supported.")  # This method will skip tests, if expression is true.
    def test_number_35(self):                                          # For example tests prepared for several operating system.
        result = calculate_number(35)                                  # And type of OS resolves which test suite will be performed.
        self.assertEqual(result, 35)

    def test_number_12780(self):
        result = calculate_number(12780)
        self.assertEqual(result, 12780)

    def tearDown(self):                             # This method will have started after every test for make report, close working file or switch off environment
        print("The testing is done, the result is posted above. Have a nice day!")

class Test_Wrong_Value(unittest.TestCase):

    def test_Wrong_Value(self):
        result = calculate_number(47)
        self.assertEqual(result, 0)

class Test_Wrong_Result(unittest.TestCase):

    def test_Wrong_Result(self):
        result = calculate_number(55)
        self.assertEqual(result, 50, 'The returned value is not equal to expected result, test is failed.')
# Third parameter of method is not necessary, but it will define action, if test is failed

    @unittest.expectedFailure
    def test_Wrong_Result2(self):
        result = calculate_number(55)
        self.assertEqual(result, 50)

if __name__ == '__main__':
    unittest.main()