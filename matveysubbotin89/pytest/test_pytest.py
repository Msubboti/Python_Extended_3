from Program_for_Testing import Testing
import pytest


def calculate_number(Number):
    dictionary = Testing(Number)
    banknotes = list(dictionary.keys())
    expected = 0
    for index in banknotes:
        expected += index * dictionary[index]
    return expected

class Test_Correct_Result():
    def test_number_2855(self):
        result = calculate_number(2855)
        assert (result == 2855)

    def test_number_35(self):
        result = calculate_number(35)
        assert (result == 35)

    def test_number_12780(self):
        result = calculate_number(12780)
        assert (result == 12780)

class Test_Wrong_Value():

    def test_Wrong_Value(self):
        result = calculate_number(47)
        assert (result == 0)

class Test_Wrong_Result():

    def test_Wrong_Result(self):
        result = calculate_number(55)
        assert (result == 50)