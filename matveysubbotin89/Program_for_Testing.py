def Testing(Number):


#print('How much money do you want to get? Number should be from 5 till 12000 grivnas')
#Number = int(input())

    banknotes = {5: 10, 10: 10, 20: 10, 50: 10, 100: 0, 200: 0, 500: 0, 1000: 0}
    limits = list()
    dict_limits = dict()

    under_limits = list()
    dict_under_limits = dict()
    Dictionary = {5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 0, 500: 0, 1000: 0}

    def sorting_number(number, variables):
        list_of_key = list(variables.keys())
        list_of_key.sort(reverse=True)

        for grivnas in list_of_key:
            if variables[grivnas] != 0:
                while number >= grivnas and variables[grivnas] > 0:
                    variables[grivnas] -= 1
                    number -= grivnas
                    Dictionary[grivnas] += 1
            else:
                while number >= grivnas:
                    number -= grivnas
                    Dictionary[grivnas] += 1
        return Dictionary


    if not (Number % min(banknotes.keys())):
        temp_banknotes = list(banknotes.keys())
        summa = 0
        for bank in temp_banknotes:
            if banknotes[bank]:
                summa += bank * banknotes[bank]
                limits.append(bank)
            else:
                under_limits.append(bank)
        limits = limits[::-1]
        under_limits = under_limits[::-1]
        for item in limits:
            dict_limits[item] = banknotes[item]
        for item in under_limits:
            dict_under_limits[item] = banknotes[item]



        if Number > summa:
            counter = 0
            while Number > summa:
                Number -= under_limits[-1]
                counter += 1
            Dictionary[under_limits[-1]] = counter

            temporary_number = under_limits[-1] * counter
            Dictionary[under_limits[-1]] = 0
            Dictionary = sorting_number(temporary_number, dict_under_limits)
            Dictionary = sorting_number(Number,dict_limits)
        else:
            Dictionary = sorting_number(Number, dict_limits)
    else:
        notes = str(banknotes.keys())
        print('Sorry, value is not correct. The banknotes: ', notes, ' are available')
    return (Dictionary)
