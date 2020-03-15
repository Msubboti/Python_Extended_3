from Program_for_Testing import Testing


def testing_Number_2855(Number=2855):  # Definition of input data
    Dictionary = Testing(Number)  # Function "Testing" was called with argument 2855"
    banknotes = list(Dictionary.keys())  # Getting list of banknotes
    print(Dictionary)  # Result has been printed after fulfilling function is done
    result = 0
    for notes in banknotes:  # How many money we got?
        result += notes * Dictionary[notes]
    if result == 2855:  # Checking and print result of test
        print('Test is pass')
    else:
        print('Test is failed')


def testing_Number_35(Number=35):
    Dictionary = Testing(Number)
    banknotes = list(Dictionary.keys())
    print(Dictionary)
    result = 0
    for notes in banknotes:
        result += notes * Dictionary[notes]
    if result == 35:
        print('Test is pass')
    else:
        print('Test is failed')


def testing_Number_12780(Number=12780):
    Dictionary = Testing(Number)
    banknotes = list(Dictionary.keys())
    print(Dictionary)
    result = 0
    for notes in banknotes:
        result += notes * Dictionary[notes]
    if result == 12780:
        print('Test is pass')
    else:
        print('Test is failed')


def testing_Wrong_Value(Number=47):      # Value is wrong, we do not have available banknotes for pay the bill.
    Dictionary = Testing(Number)         # In this case, function return text message, and does not start to
    banknotes = list(Dictionary.keys())  # calculate. The every banknote in dictionary has value "0"
    print(Dictionary)                    # , so the sum is equal to zero also.
    result = 0
    for notes in banknotes:
        result += notes * Dictionary[notes]
    if result == 0:                      # The result of test should be 0
        print('Test is pass')
    else:
        print('Test is failed')


def testing_Wrong_Result(Number=55):     # In this test we will compare returning
    Dictionary = Testing(Number)         # result of function with wrong number.
    banknotes = list(Dictionary.keys())
    print(Dictionary)
    result = 0
    for notes in banknotes:
        result += notes * Dictionary[notes]
    if result == 50:                      # This mistake was made intentionally,
        print('Test is pass')             # for checking negative test
    else:
        print('Test is failed')


testing_Number_2855()
testing_Number_35()
testing_Number_12780()
testing_Wrong_Value()
testing_Wrong_Result()
