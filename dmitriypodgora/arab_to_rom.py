romans = dict(I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 100)

def p_rom (roman):
    result = 0
    for i, c in enumerate(roman):
        if i + 1 < len(roman) and romans[roman[i]] < romans[roman[i+1]]:
            result -= romans[roman[i]]
        else:
            result += romans[roman[i]]
    return result
p_rom("I")
print(p_rom('CVV'))