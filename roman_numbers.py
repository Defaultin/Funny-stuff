table = {
    'M': 1000, 'CM': 900,
    'D': 500,  'CD': 400,
    'C': 100,  'XC': 90,
    'L': 50,   'XL': 40,
    'X': 10,   'IX': 9, 
    'V': 5,    'IV': 4,
    'I': 1
}


def int2roman(number):
    '''1989 -> MCMLXXXIX'''
    roman = ''
    while number:
        for letter, digit in table.items():
            if number >= digit:
                roman += letter * (number // digit)
                number %= digit
    return roman


def roman2int(roman):
    '''MCMLXXXIX -> 1989'''
    number = 0
    for i in range(len(roman)):
        if i and table[roman[i-1]] < table[roman[i]]:
            number += table[roman[i]] - 2 * table[roman[i-1]]
        else:
            number += table[roman[i]]
    return number


if __name__ == '__main__':
    for i in range(1, 10 ** 4): 
        assert roman2int(int2roman(i)) == i